import base64
import json
import os
import streamlit as st

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E ESTILIZAÇÃO CSS (VISUAL NEON E TIPOGRAFIA EM NEGRITO)
# ==============================================================================
st.set_page_config(
    page_title="ENEM História Game Studio",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&display=swap');

    html, body, [class*="css"], .stApp {
        background-color: #070A12 !important;
        color: #FFFFFF !important;
        font-family: 'Montserrat', sans-serif !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-weight: 900 !important;
        letter-spacing: 0.5px;
    }

    /* Top Bar Status */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #0F1526;
        padding: 16px 28px;
        border-radius: 16px;
        border: 2px solid #1E2942;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    
    .status-badge {
        background-color: #182238;
        padding: 8px 18px;
        border-radius: 25px;
        font-weight: 900 !important;
        color: #FFC107;
        border: 2px solid #2A3B5C;
        font-size: 15px;
    }

    /* Cartões de Categoria */
    .card-geral {
        background: linear-gradient(180deg, #0A1C38 0%, #061021 100%);
        border: 3px solid #0088FF;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 136, 255, 0.3);
    }
    
    .card-brasil {
        background: linear-gradient(180deg, #093325 0%, #051A13 100%);
        border: 3px solid #00E676;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 230, 118, 0.3);
    }

    /* Caixa do Desafio */
    .question-box {
        background-color: #0F1526;
        border: 2px solid #1E2942;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        font-weight: 800 !important;
    }

    /* Dica Teórica Amarela */
    .dica-box {
        background-color: #FFD54F;
        color: #000000;
        padding: 18px 22px;
        border-radius: 14px;
        font-weight: 900 !important;
        font-size: 15px;
        margin-bottom: 20px;
        border-left: 8px solid #FFA000;
        box-shadow: 0 4px 15px rgba(255, 213, 79, 0.2);
    }

    /* Cartões de Sucesso e Erro */
    .success-card {
        background: radial-gradient(circle, #08261C 0%, #03120D 100%);
        border: 3px solid #00E676;
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 30px rgba(0, 230, 118, 0.4);
    }
    
    .error-card {
        background: radial-gradient(circle, #3D0C17 0%, #170308 100%);
        border: 3px solid #FF3366;
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 30px rgba(255, 51, 102, 0.4);
    }

    /* Botões Principais */
    .stButton>button {
        background: linear-gradient(180deg, #FFCA28 0%, #FFA000 100%) !important;
        color: #000000 !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 14px 28px !important;
        font-size: 16px !important;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 160, 0, 0.4);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(255, 160, 0, 0.6);
    }

    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        font-weight: 800 !important;
        border-radius: 12px !important;
        background-color: #0F1526 !important;
        color: #FFFFFF !important;
        border: 2px solid #1E2942 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. BANCO DE DADOS LOCAL (100% LIMPO - SEM BOT NENHUM)
# ==============================================================================
DB_FILE = "banco_jogadores.json"


def carregar_banco_dados():
    if not os.path.exists(DB_FILE):
        dados_iniciais = {"jogadores": {}}
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(dados_iniciais, f, ensure_ascii=False, indent=4)
        return dados_iniciais
    else:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)


def salvar_banco_dados(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)


db = carregar_banco_dados()

# ==============================================================================
# 3. ESTADOS DA SESSÃO
# ==============================================================================
if "usuario_atual" not in st.session_state:
    st.session_state.usuario_atual = None
if "tela" not in st.session_state:
    st.session_state.tela = "login"
if "categoria_ativa" not in st.session_state:
    st.session_state.categoria_ativa = "Geral"
if "jogo_id" not in st.session_state:
    st.session_state.jogo_id = 0
if "fase_jogo" not in st.session_state:
    st.session_state.fase_jogo = "pergunta"

# ==============================================================================
# 4. BASE DE DADOS DOS 30 JOGOS (COM IMAGENS EM TODAS AS QUESTÕES)
# ==============================================================================
JOGOS_GERAL = [
    {
        "id": 1,
        "nome": "1. Antiguidade Clássica",
        "sub": "Atenas vs Esparta",
        "dica": "💡 DICA ENEM: Atenas valorizava a Eclésia e a democracia direta. Esparta focava no militarismo (agoge) e na oligarquia.",
        "pergunta": "Qual cidade-estado grega fundamentava sua sociedade no militarismo desde a infância (agoge) e no poder oligárquico?",
        "opcoes": ["Atenas", "Esparta", "Roma", "Tebas"],
        "correta": "Esparta",
        "explicacao": "Esparta estruturou a sua sociedade na preparação militar e no controlo oligárquico rígido.",
        "img": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
    },
    {
        "id": 2,
        "nome": "2. Idade Média",
        "sub": "A Crise Feudal",
        "dica": "💡 DICA ENEM: A Peste Negra (século XIV) provocou escassez de mão de obra e acelerou a crise do sistema feudal.",
        "pergunta": "Qual evento do século XIV dizimou um terço da população europeia e abalou o feudalismo?",
        "opcoes": ["Peste Negra", "Guerra dos Cenzos", "Queda de Roma", "Renascimento"],
        "correta": "Peste Negra",
        "explicacao": "A escassez de camponeses enfraqueceu os laços de servidão impostos pelos senhores feudais.",
        "img": "https://images.unsplash.com/photo-1599739291060-4578e77dac5d?w=800",
    },
    {
        "id": 3,
        "nome": "3. Renascimento Cultural",
        "sub": "Humanismo & Razão",
        "dica": "💡 DICA ENEM: O Antropocentrismo colocou o ser humano e a razão no centro das atenções, opondo-se ao Teocentrismo medieval.",
        "pergunta": "Qual conceito renascentista colocava a figura e a capacidade humana no centro do conhecimento?",
        "opcoes": ["Teocentrismo", "Antropocentrismo", "Feudalismo", "Escolástica"],
        "correta": "Antropocentrismo",
        "explicacao": "O Antropocentrismo contrapôs-se ao Teocentrismo, valorizando a razão humana e a observação da natureza.",
        "img": "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?w=800",
    },
    {
        "id": 4,
        "nome": "4. Reformas Religiosas",
        "sub": "Lutero e Calvino",
        "dica": "💡 DICA ENEM: O Calvinismo associava a salvação à Teoria da Predestinação e valorizava o trabalho rigoroso e a prosperidade.",
        "pergunta": "Qual reformador religioso relacionava o sucesso profissional e o trabalho à Doutrina da Predestinação?",
        "opcoes": ["João Calvino", "Martinho Lutero", "Henrique VIII", "Inácio de Loyola"],
        "correta": "João Calvino",
        "explicacao": "O calvinismo foi amplamente aceito pela burguesia por valorizar o trabalho e a prosperidade econômica.",
        "img": "https://images.unsplash.com/photo-1548625149-fc4a29cf7092?w=800",
    },
    {
        "id": 5,
        "nome": "5. Iluminismo",
        "sub": "A Divisão dos Poderes",
        "dica": "💡 DICA ENEM: Montesquieu defendeu a divisão do Estado em Executivo, Legislativo e Judiciário para conter o Absolutismo.",
        "pergunta": "Qual pensador iluminista teorizou a divisão do Estado em três poderes independentes?",
        "opcoes": ["Montesquieu", "Voltaire", "Rousseau", "John Locke"],
        "correta": "Montesquieu",
        "explicacao": "A tripartição dos poderes foi elaborada por Montesquieu na obra 'O Espírito das Leis'.",
        "img": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=800",
    },
    {
        "id": 6,
        "nome": "6. Revolução Industrial",
        "sub": "A Era do Carvão",
        "dica": "💡 DICA ENEM: A 1ª Revolução Industrial baseou-se na energia a vapor e no carvão mineral na Inglaterra.",
        "pergunta": "Qual fonte de energia foi o grande motor da Primeira Revolução Industrial?",
        "opcoes": ["Carvão Mineral", "Petróleo", "Energia Eólica", "Eletricidade"],
        "correta": "Carvão Mineral",
        "explicacao": "O carvão mineral alimentava as caldeiras das máquinas a vapor e das indústrias inglesas.",
        "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800",
    },
    {
        "id": 7,
        "nome": "7. Revolução Francesa",
        "sub": "O Terror Jacobino",
        "dica": "💡 DICA ENEM: Os Jacobinos (Robespierre) lideraram a fase mais radical e popular da Revolução Francesa (O Terror).",
        "pergunta": "Qual grupo político esteve à frente das execuções na fase mais radical da Revolução Francesa?",
        "opcoes": ["Jacobinos", "Girondinos", "Absolutistas", "Fagundistas"],
        "correta": "Jacobinos",
        "explicacao": "Liderados por Robespierre, os Jacobinos guilhotinaram opositores no período do Terror.",
        "img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800",
    },
    {
        "id": 8,
        "nome": "8. Neocolonialismo",
        "sub": "A Partilha da África",
        "dica": "💡 DICA ENEM: A Conferência de Berlim (1884-1885) partilhou a África entre potências europeias sem respeitar etnias locais.",
        "pergunta": "Qual conferência internacional oficializou a partilha do continente africano entre as potências europeias?",
        "opcoes": ["Conferência de Berlim", "Congresso de Viena", "Tratado de Versalhes", "Pacto de Varsóvia"],
        "correta": "Conferência de Berlim",
        "explicacao": "A partilha de Berlim dividiu o território africano segundo interesses imperialistas.",
        "img": "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=800",
    },
    {
        "id": 9,
        "nome": "9. Primeira Guerra",
        "sub": "O Estopim de Sarajevo",
        "dica": "💡 DICA ENEM: O estopim da 1ª Guerra foi o assassinato do arquiduque Francisco Ferdinando em Sarajevo (1914).",
        "pergunta": "Qual evento provocou o acionamento das alianças militares e o início da Primeira Guerra Mundial?",
        "opcoes": ["O assassinato de Francisco Ferdinando", "A queda do Muro de Berlim", "A crise dos mísseis", "A invasão da Polônia"],
        "correta": "O assassinato de Francisco Ferdinando",
        "explicacao": "O atentado de Sarajevo em 1914 ativou o sistema de alianças na Europa.",
        "img": "https://images.unsplash.com/photo-1579912437766-789233630f0f?w=800",
    },
    {
        "id": 10,
        "nome": "10. Revolução Russa",
        "sub": "Teses de Abril",
        "dica": "💡 DICA ENEM: O lema bolchevique 'Paz, Pão e Terra' sintetizava a saída da guerra, combate à fome e reforma agrária.",
        "pergunta": "Qual lema popular sintetizou o programa dos bolcheviques liderados por Lênin em 1917?",
        "opcoes": ["Paz, Pão e Terra", "Liberdade, Igualdade e Fraternidade", "Ordem e Progresso", "Trabalho e Pátria"],
        "correta": "Paz, Pão e Terra",
        "explicacao": "O slogan atendeu aos anseios populares russos durante o processo revolucionário.",
        "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800",
    },
    {
        "id": 11,
        "nome": "11. Crise de 1929",
        "sub": "O New Deal",
        "dica": "💡 DICA ENEM: O New Deal aplicou intervenção estatal na economia (Keynesianismo) para combater a Grande Depressão.",
        "pergunta": "Qual plano aplicou obras públicas e direitos sociais para recuperar os EUA na crise de 1929?",
        "opcoes": ["New Deal", "Plano Marshall", "Doutrina Truman", "Plano Quinquenal"],
        "correta": "New Deal",
        "explicacao": "Franklin Roosevelt usou o New Deal para reerguer a economia americana com regulação estatal.",
        "img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800",
    },
    {
        "id": 12,
        "nome": "12. Nazifascismo",
        "sub": "Regimes Totalitários",
        "dica": "💡 DICA ENEM: O Nazifascismo fundamentava-se no totalitarismo, culto ao líder, ultranacionalismo e anticomunismo.",
        "pergunta": "Qual característica NÃO pertence ao ideário e atuação do Nazifascismo?",
        "opcoes": ["Defesa da democracia liberal", "Culto à figura do líder supremo", "Ultranacionalismo agressivo", "Anticomunismo fervoroso"],
        "correta": "Defesa da democracia liberal",
        "explicacao": "Os regimes nazifascistas destruíram a democracia liberal e o pluralismo político.",
        "img": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=800",
    },
    {
        "id": 13,
        "nome": "13. Segunda Guerra",
        "sub": "Virada em Stalingrado",
        "dica": "💡 DICA ENEM: Stalingrado foi o ponto de virada na Frente Oriental, iniciando o recuo das tropas alemãs.",
        "pergunta": "Qual batalha é considerada o ponto de virada decisivo contra os nazistas na Europa Oriental?",
        "opcoes": ["Batalha de Stalingrado", "Batalha de Midway", "Ataque a Pearl Harbor", "Dia D"],
        "correta": "Batalha de Stalingrado",
        "explicacao": "A vitória soviética em Stalingrado forçou a Alemanha nazista a recuar na guerra.",
        "img": "https://images.unsplash.com/photo-1579912437766-789233630f0f?w=800",
    },
    {
        "id": 14,
        "nome": "14. Guerra Fria",
        "sub": "O Bloco Ocidental",
        "dica": "💡 DICA ENEM: A OTAN foi criada como a aliança militar do bloco capitalista liderado pelos EUA.",
        "pergunta": "Qual aliança militar foi criada pelos países ocidentais capitalistas em 1949?",
        "opcoes": ["OTAN", "Pacto de Varsóvia", "União Europeia", "Liga das Nações"],
        "correta": "OTAN",
        "explicacao": "A OTAN reuniu a defesa militar dos países capitalistas contra o avanço soviético.",
        "img": "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=800",
    },
    {
        "id": 15,
        "nome": "15. Mundo Contemporâneo",
        "sub": "Fim da URSS",
        "dica": "💡 DICA ENEM: As reformas Glasnost e Perestroika aceleraram o processo de dissolução da União Soviética.",
        "pergunta": "Quais foram as reformas promovidas por Mikhail Gorbachev na década de 1980 na URSS?",
        "opcoes": ["Perestroika e Glasnost", "New Deal e Fair Deal", "Plano Marshall e Doutrina Truman", "Plano Real e URV"],
        "correta": "Perestroika e Glasnost",
        "explicacao": "A abertura política (Glasnost) e a reestruturação econômica (Perestroika) culminaram no fim da URSS.",
        "img": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800",
    },
]

JOGOS_BRASIL = [
    {
        "id": 1,
        "nome": "1. Período Pré-Colonial",
        "sub": "Pau-Brasil e Escambo",
        "dica": "💡 DICA ENEM: No Período Pré-Colonial (1500-1530), a exploração do pau-brasil baseava-se no escambo com os indígenas.",
        "pergunta": "Qual era o sistema de troca direta por trabalho indígena sem uso de moedas no Período Pré-Colonial?",
        "opcoes": ["Escambo", "Mita", "Encomienda", "Servidão"],
        "correta": "Escambo",
        "explicacao": "O escambo garantia a extração da madeira trocando o trabalho indígena por ferramentas de ferro e objetos.",
        "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800",
    },
    {
        "id": 2,
        "nome": "2. Brasil Colônia",
        "sub": "Engenho de Açúcar",
        "dica": "💡 DICA ENEM: A economia do açúcar apoiava-se no modelo de Plantation: latifúndio, monocultura e escravidão.",
        "pergunta": "Qual modelo agrícola caracterizava a produção do açúcar no Nordeste colonial?",
        "opcoes": ["Plantation monocultor com escravidão", "Minifúndios policultores familiares", "Cooperativas de trabalhadores livres", "Feudalismo autossuficiente"],
        "correta": "Plantation monocultor com escravidão",
        "explicacao": "A Plantation unia grandes propriedades, monocultura de exportação e escravidão.",
        "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800",
    },
    {
        "id": 3,
        "nome": "3. Ciclo do Ouro",
        "sub": "A Derrama",
        "dica": "💡 DICA ENEM: A cobrança forçada de impostos atrasados (Derrama) provocou a Inconfidência Mineira.",
        "pergunta": "Qual imposto forçado sobre impostos em atraso revoltou a Capitania de Minas Gerais?",
        "opcoes": ["Derrama", "Quinto", "Capitação", "Dízimo"],
        "correta": "Derrama",
        "explicacao": "A ameaça da aplicação da Derrama levou a elite de Vila Rica a conspirar contra a Coroa em 1789.",
        "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800",
    },
    {
        "id": 4,
        "nome": "4. Movimentos Emancipatórios",
        "sub": "Conjuração Baiana",
        "dica": "💡 DICA ENEM: A Conjuração Baiana (1798) destacou-se pelo caráter popular e pela defesa do fim da escravidão.",
        "pergunta": "Qual movimento colonial teve forte participação popular e exigiu o fim da escravidão?",
        "opcoes": ["Conjuração Baiana", "Inconfidência Mineira", "Guerra dos Mascates", "Guerra dos Emboabas"],
        "correta": "Conjuração Baiana",
        "explicacao": "Inspirada na Revolução Francesa, a Conjuração Baiana trazia pautas sociais e antirracistas.",
        "img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800",
    },
    {
        "id": 5,
        "nome": "5. Período Joanino",
        "sub": "Abertura dos Portos",
        "dica": "💡 DICA ENEM: A Abertura dos Portos (1808) rompeu na prática o Pacto Colonial.",
        "pergunta": "O decreto de Abertura dos Portos em 1808 encerrou qual restrição comercial colonial?",
        "opcoes": ["O Pacto Colonial (Exclusivo Metropolitano)", "A proibição do cultivo do café", "O imposto do Quinto do Ouro", "A escravidão indígena"],
        "correta": "O Pacto Colonial (Exclusivo Metropolitano)",
        "explicacao": "A Abertura dos Portos permitiu ao Brasil comerciar diretamente com nações amigas.",
        "img": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=800",
    },
    {
        "id": 6,
        "nome": "6. Primeiro Reinado",
        "sub": "Poder Moderador",
        "dica": "💡 DICA ENEM: A Constituição de 1824 criou o Poder Moderador, exclusivo do imperador D. Pedro I.",
        "pergunta": "Qual poder exclusivo do Imperador na Constituição de 1824 permitia intervir sobre os outros poderes?",
        "opcoes": ["Poder Moderador", "Poder Absoluto", "Poder Regencial", "Poder Executivo Imperial"],
        "correta": "Poder Moderador",
        "explicacao": "O Poder Moderador garantiu a centralização de autoridade nas mãos de D. Pedro I.",
        "img": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
    },
    {
        "id": 7,
        "nome": "7. Período Regencial",
        "sub": "Revolta dos Malês",
        "dica": "💡 DICA ENEM: A Revolta dos Malês (1835) foi organizada por escravizados e libertos muçulmanos em Salvador.",
        "pergunta": "Qual revolta em Salvador (1835) foi liderada por africanos de religião islâmica?",
        "opcoes": ["Revolta dos Malês", "Cabanagem", "Sabinada", "Balaiada"],
        "correta": "Revolta dos Malês",
        "explicacao": "Os malês usaram a escrita em árabe para organizar o levante contra a escravidão.",
        "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800",
    },
    {
        "id": 8,
        "nome": "8. Segundo Reinado",
        "sub": "Oeste Paulista e Café",
        "dica": "💡 DICA ENEM: O Oeste Paulista destacou-se pela modernização do café e pelo uso da mão de obra imigrante.",
        "pergunta": "Qual região tornou-se o centro produtor de café e de atração de imigrantes no Império?",
        "opcoes": ["Oeste Paulista", "Vale do Paraíba", "Recôncavo Baiano", "Zona da Mata"],
        "correta": "Oeste Paulista",
        "explicacao": "O Oeste Paulista utilizou ferrovias e a transição para o trabalho livre assalariado imigrante.",
        "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800",
    },
    {
        "id": 9,
        "nome": "9. Leis Abolicionistas",
        "sub": "Fim do Tráfico",
        "dica": "💡 DICA ENEM: A Lei Eusébio de Queirós (1850) extinguiu o tráfico transatlântico de escravizados.",
        "pergunta": "Qual lei de 1850 proibiu definitivamente o tráfico negreiro transatlântico para o Brasil?",
        "opcoes": ["Lei Eusébio de Queirós", "Lei do Ventre Livre", "Lei Áurea", "Lei dos Sexagenários"],
        "correta": "Lei Eusébio de Queirós",
        "explicacao": "A extinção do tráfico redirecionou recursos financeiros para a modernização do país.",
        "img": "https://images.unsplash.com/photo-1599739291060-4578e77dac5d?w=800",
    },
    {
        "id": 10,
        "nome": "10. Primeira República",
        "sub": "Coronelismo",
        "dica": "💡 DICA ENEM: O Voto de Cabresto garantiu o controlo eleitoral oligárquico durante a República Velha.",
        "pergunta": "Qual nome era dado ao voto controlado coercitivamente pelos coronéis locais?",
        "opcoes": ["Voto de Cabresto", "Voto Censitário", "Sufrágio Secreto", "Voto Distrital"],
        "correta": "Voto de Cabresto",
        "explicacao": "Os coronéis usavam violência e trocas de favores para assegurar os votos da população.",
        "img": "https://images.unsplash.com/photo-1547471080-7cc2caa01a7e?w=800",
    },
    {
        "id": 11,
        "nome": "11. Era Vargas",
        "sub": "O DIP",
        "dica": "💡 DICA ENEM: O DIP foi o órgão de propaganda e censura oficial no Estado Novo de Vargas.",
        "pergunta": "Qual órgão exerceu a censura e a propaganda no Estado Novo (1937-1945)?",
        "opcoes": ["DIP (Departamento de Imprensa e Propaganda)", "DOPS", "SNI", "CLT"],
        "correta": "DIP (Departamento de Imprensa e Propaganda)",
        "explicacao": "O DIP promovia a exaltação a Getúlio Vargas e controlava a imprensa, rádio e cinema.",
        "img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800",
    },
    {
        "id": 12,
        "nome": "12. Período Populista",
        "sub": "Plano de Metas",
        "dica": "💡 DICA ENEM: Juscelino Kubitschek promoveu a meta '50 anos em 5' construindo Brasília e atraindo indústrias.",
        "pergunta": "Qual foi o slogan de desenvolvimento adotado no governo Juscelino Kubitschek?",
        "opcoes": ["50 anos em 5", "Brasil Ame-o ou Deixe-o", "Ordem e Progresso", "Paz e Trabalho"],
        "correta": "50 anos em 5",
        "explicacao": "O Plano de Metas priorizou a construção de Brasília, transporte rodoviário e energia.",
        "img": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=800",
    },
    {
        "id": 13,
        "nome": "13. Ditadura Militar",
        "sub": "O AI-5",
        "dica": "💡 DICA ENEM: O AI-5 (1968) decretou a fase mais repressiva da Ditadura Militar, suspendendo garantias judiciais.",
        "pergunta": "Qual ato fechou o Congresso e suspendeu o habeas corpus na Ditadura Militar em 1968?",
        "opcoes": ["AI-5", "AI-1", "Lei de Anistia", "Estatuto Militar"],
        "correta": "AI-5",
        "explicacao": "O AI-5 suspendeu garantias individuais e permitiu a cassação de mandatos políticos.",
        "img": "https://images.unsplash.com/photo-1579912437766-789233630f0f?w=800",
    },
    {
        "id": 14,
        "nome": "14. Redemocratização",
        "sub": "Constituição de 1988",
        "dica": "💡 DICA ENEM: A Carta de 1988 ficou conhecida como 'Constituição Cidadã' por garantir direitos sociais amplos.",
        "pergunta": "Como ficou conhecida a Constituição de 1988 pelas suas conquistas sociais?",
        "opcoes": ["Constituição Cidadã", "Carta Magna do Povo", "Outorga de 88", "Constituição da Mandioca"],
        "correta": "Constituição Cidadã",
        "explicacao": "A Constituição de 1988 consolidou o retorno à democracia e os direitos fundamentais.",
        "img": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800",
    },
    {
        "id": 15,
        "nome": "15. Brasil Contemporâneo",
        "sub": "Plano Real",
        "dica": "💡 DICA ENEM: O Plano Real (1994) acabou com a hiperinflação através da introdução da URV e do Real.",
        "pergunta": "Qual plano econômico de 1994 conseguiu controlar a hiperinflação no Brasil?",
        "opcoes": ["Plano Real", "Plano Cruzado", "Plano Collor", "Plano Bresser"],
        "correta": "Plano Real",
        "explicacao": "O Plano Real trouxe estabilidade à moeda e recuperou o poder de compra dos brasileiros.",
        "img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800",
    },
]

# ==============================================================================
# 5. BARRA SUPERIOR DINÂMICA
# ==============================================================================
if st.session_state.usuario_atual and st.session_state.usuario_atual in db["jogadores"]:
    u = db["jogadores"][st.session_state.usuario_atual]
    xp_val = u["xp"]
    moedas_val = u["moedas"]
    ofensiva_val = u["ofensiva"]
    nome_exib = u["nome_exibicao"]
    
    if u.get("foto_base64"):
        avatar_exib = "📷"
    else:
        avatar_exib = u.get("avatar", "🎓")
else:
    xp_val = 0
    moedas_val = 0
    ofensiva_val = 0
    nome_exib = "Sem Perfil Ativo"
    avatar_exib = "👤"

st.markdown(
    f"""
    <div class="top-bar">
        <div style="font-size: 20px; font-weight: 900; color: #FFC107;">
            {avatar_exib} {nome_exib.upper()}
        </div>
        <div>
            <span class="status-badge">🔥 {ofensiva_val} DIAS</span>
            <span class="status-badge" style="margin-left: 10px;">🪙 {moedas_val}</span>
            <span class="status-badge" style="margin-left: 10px; color: #00E676;">⚡ {xp_val} XP</span>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# Menu Superior
m1, m2, m3, m4, m5 = st.columns(5)
if m1.button("🏠 INÍCIO"):
    st.session_state.tela = "inicio"
    st.rerun()
if m2.button("🎮 JOGOS"):
    if st.session_state.usuario_atual:
        st.session_state.tela = "categorias"
    else:
        st.session_state.tela = "login"
    st.rerun()
if m3.button("🏆 RANKING"):
    st.session_state.tela = "ranking"
    st.rerun()
if m4.button("🎖️ CONQUISTAS"):
    st.session_state.tela = "conquistas"
    st.rerun()
if m5.button("👤 PERFIL"):
    if st.session_state.usuario_atual:
        st.session_state.tela = "perfil"
    else:
        st.session_state.tela = "login"
    st.rerun()

st.markdown("---")

# ==============================================================================
# 6. GERENCIADOR DE TELAS E FLUXO DO JOGO
# ==============================================================================

# --- TELA: LOGIN E CADASTRO DE PERFIL ---
if st.session_state.tela == "login":
    st.subheader("🔑 CRIAR PERFIL OU ENTRAR NO JOGO")
    st.caption("Cadastre o seu nome e foto para salvar o seu XP real na tabela de classificação!")

    tab_login, tab_cadastro = st.tabs(["Entrar com Perfil Existente", "Criar Novo Perfil Real"])

    with tab_login:
        if len(db["jogadores"]) > 0:
            nick_login = st.selectbox("Selecione o seu utilizador:", options=list(db["jogadores"].keys()))
            if st.button("🚀 ENTRAR NO JOGO"):
                st.session_state.usuario_atual = nick_login
                st.session_state.tela = "inicio"
                st.rerun()
        else:
            st.info("Ainda não existem utilizadores criados. Registe o seu perfil na aba ao lado!")

    with tab_cadastro:
        novo_username = st.text_input("Username único (ex: joao_enem):").strip().lower()
        novo_nome = st.text_input("Seu Nome de Exibição:")
        nova_bio = st.text_input("Sua Meta de Estudo:", value="Aprovação no ENEM!")
        
        novo_avatar = st.selectbox("Escolha um Ícone de Avatar:", ["🎓", "⚔️", "👑", "🚀", "🏹", "🦁", "☕"])
        
        st.write("**Foto de Perfil Pessoal (Opcional - Escolher da Galeria do seu Dispositivo):**")
        foto_upload = st.file_uploader("Carregue uma foto da sua galeria:", type=["png", "jpg", "jpeg"])
        
        foto_b64 = None
        if foto_upload is not None:
            foto_bytes = foto_upload.read()
            foto_b64 = base64.b64encode(foto_bytes).decode("utf-8")
            st.image(foto_upload, width=120, caption="Pré-visualização da Foto")

        if st.button("✨ CADASTRAR MEU PERFIL"):
            if not novo_username or not novo_nome:
                st.error("Por favor, preencha o Username e o Nome de Exibição!")
            elif novo_username in db["jogadores"]:
                st.error("Este Username já está registado! Escolha outro.")
            else:
                db["jogadores"][novo_username] = {
                    "nome_exibicao": novo_nome,
                    "avatar": novo_avatar,
                    "foto_base64": foto_b64,
                    "bio": nova_bio,
                    "xp": 0,
                    "moedas": 0,
                    "ofensiva": 1,
                    "jogos_concluidos": 0,
                    "acertos": 0,
                    "erros": 0,
                }
                salvar_banco_dados(db)
                st.session_state.usuario_atual = novo_username
                st.success("Perfil registado com sucesso!")
                st.session_state.tela = "inicio"
                st.rerun()

# --- TELA: INÍCIO ---
elif st.session_state.tela == "inicio":
    col_banner, col_info = st.columns([2, 1])

    with col_banner:
        st.markdown(
            """
            <div style="background: linear-gradient(90deg, #0D1B2A 0%, #1B263B 100%); padding: 40px; border-radius: 20px; border: 2px solid #1E2942;">
                <h1 style="color: #FFC107; font-size: 40px; margin-bottom: 0;">👑 ENEM HISTÓRIA GAME</h1>
                <p style="color: #8D99AE; font-size: 16px; font-weight: 800;">APRENDA • JOGUE • CONQUISTE</p>
                <p style="margin-top: 15px; font-size: 16px;"><b>30 jogos completos com imagens estáveis</b>, dicas teóricas e ranking totalmente real integrado!</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("▶️ COMEÇAR AGORA"):
            if st.session_state.usuario_atual:
                st.session_state.tela = "categorias"
            else:
                st.session_state.tela = "login"
            st.rerun()

    with col_info:
        st.markdown(
            """
            <div style="background-color: #0F1526; padding: 25px; border-radius: 20px; border: 2px solid #1E2942;">
                <h3 style="color: #FFC107; margin-top: 0;">💡 Dica para a Prova</h3>
                <p style="font-size: 15px; font-weight: 800;">Lembre-se: As questões do ENEM conectam frequentemente acontecimentos históricos com cidadania, direitos humanos e matrizes culturais.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

# --- TELA: SELEÇÃO DE CATEGORIAS ---
elif st.session_state.tela == "categorias":
    st.subheader("ESCOLHA A CATEGORIA DE ESTUDO")
    st.caption("Selecione abaixo para abrir a grade dos 30 jogos:")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="card-geral">
                <h2>🌍 HISTÓRIA GERAL</h2>
                <h3 style="color: #0088FF; font-size: 30px;">15 JOGOS</h3>
                <p style="font-weight: 800;">Da Grécia Antiga e Roma até a Guerra Fria e a Globalização.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("JOGAR HISTÓRIA GERAL ➔"):
            st.session_state.categoria_ativa = "Geral"
            st.session_state.tela = "grade_jogos"
            st.rerun()

    with c2:
        st.markdown(
            """
            <div class="card-brasil">
                <h2>🇧🇷 HISTÓRIA DO BRASIL</h2>
                <h3 style="color: #00E676; font-size: 30px;">15 JOGOS</h3>
                <p style="font-weight: 800;">Do Período Pré-Colonial ao Império, Ditadura Militar e Nova República.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("JOGAR HISTÓRIA DO BRASIL ➔"):
            st.session_state.categoria_ativa = "Brasil"
            st.session_state.tela = "grade_jogos"
            st.rerun()

# --- TELA: GRADE DOS 30 JOGOS ---
elif st.session_state.tela == "grade_jogos":
    st.subheader(f"🌐 HISTÓRIA {st.session_state.categoria_ativa.upper()}")
    st.caption("Escolha um jogo abaixo para iniciar:")

    jogos_lista = (
        JOGOS_GERAL
        if st.session_state.categoria_ativa == "Geral"
        else JOGOS_BRASIL
    )

    for row in range(3):
        cols = st.columns(5)
        for col_idx in range(5):
            idx = row * 5 + col_idx
            if idx < len(jogos_lista):
                jogo = jogos_lista[idx]
                with cols[col_idx]:
                    st.markdown(
                        f"""
                        <div style="background-color: #0F1526; border: 2px solid #1E2942; padding: 18px; border-radius: 16px; text-align: center;">
                            <div style="font-size: 24px;">🏛️</div>
                            <small style="font-size: 12px; font-weight: 800;"><b>{jogo['nome']}</b></small><br>
                            <span style="color: #00E676; font-size: 11px; font-weight: 900;">⭐ LIBERADO</span>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
                    st.write("")
                    if st.button("JOGAR", key=f"btn_fase_sel_{idx}"):
                        st.session_state.jogo_id = idx
                        st.session_state.tela = "gameplay"
                        st.session_state.fase_jogo = "pergunta"
                        st.rerun()

# --- TELA: GAMEPLAY ESTÁVEL (COM IMAGENS FIXAS E SEM BUGS) ---
elif st.session_state.tela == "gameplay":
    jogos_lista = (
        JOGOS_GERAL
        if st.session_state.categoria_ativa == "Geral"
        else JOGOS_BRASIL
    )
    jogo = jogos_lista[st.session_state.jogo_id]

    if st.session_state.fase_jogo == "pergunta":
        st.subheader(f"JOGO: {jogo['nome'].upper()} | {jogo['sub']}")

        col_img, col_q = st.columns([1, 1.2])

        with col_img:
            # Imagem estável sem recarregamentos por segundo
            st.image(jogo["img"], use_container_width=True)
            st.markdown(
                f"<div class='dica-box'>{jogo['dica']}</div>",
                unsafe_allow_html=True,
            )

        with col_q:
            st.markdown(
                f"""
                <div class="question-box">
                    <h3 style="margin-top: 0; font-weight: 900;">{jogo['pergunta']}</h3>
                </div>
            """,
                unsafe_allow_html=True,
            )

            for opt in jogo["opcoes"]:
                if st.button(opt, key=f"btn_opt_val_{opt}"):
                    if st.session_state.usuario_atual in db["jogadores"]:
                        u = db["jogadores"][st.session_state.usuario_atual]
                        if opt == jogo["correta"]:
                            u["xp"] += 100
                            u["moedas"] += 30
                            u["acertos"] += 1
                            u["jogos_concluidos"] += 1
                            salvar_banco_dados(db)
                            st.session_state.fase_jogo = "acertou"
                        else:
                            u["erros"] += 1
                            salvar_banco_dados(db)
                            st.session_state.fase_jogo = "errou"
                    st.rerun()

    # --- TELA ACERTOU ---
    elif st.session_state.fase_jogo == "acertou":
        st.markdown(
            f"""
            <div class="success-card">
                <h1 style="color: #00E676; font-size: 45px; margin-top: 0;">✅ RESPOSTA CERTA!</h1>
                <p style="font-size: 17px; font-weight: 800;">{jogo['explicacao']}</p>
                <br>
                <div style="font-size: 20px; font-weight: 900; color: #FFC107;">
                    ⚡ + 100 XP &nbsp;&nbsp;&nbsp;&nbsp; 🪙 + 30 MOEDAS
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("AVANÇAR E CONCLUIR FASE ➔"):
            st.session_state.fase_jogo = "fim"
            st.rerun()

    # --- TELA ERROU ---
    elif st.session_state.fase_jogo == "errou":
        st.markdown(
            f"""
            <div class="error-card">
                <h1 style="color: #FF3366; font-size: 45px; margin-top: 0;">❌ RESPOSTA INCORRETA</h1>
                <p style="font-size: 17px; font-weight: 800;">Revise o conceito abaixo para a próxima tentativa:</p>
                <div style="background-color: #24050C; padding: 20px; border-radius: 14px; border: 2px solid #FF3366; color: #FFFFFF; font-weight: 800;">
                    {jogo['dica']}
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("🔄 TENTAR NOVAMENTE"):
            st.session_state.fase_jogo = "pergunta"
            st.rerun()

    # --- TELA FIM DO JOGO ---
    elif st.session_state.fase_jogo == "fim":
        st.balloons()
        c_res, c_quote = st.columns(2)

        with c_res:
            st.markdown(
                """
                <div style="background-color: #0F1526; padding: 35px; border-radius: 20px; text-align: center; border: 2px solid #1E2942;">
                    <h2 style="color: #FFC107; margin-top: 0;">🏆 DESAFIO CONCLUÍDO!</h2>
                    <h1 style="color: #00E676; font-size: 55px;">100%</h1>
                    <p style="color: #8D99AE; font-weight: 800;">Sua pontuação de XP foi atualizada no seu perfil oficial!</p>
                    <hr style="border-color: #1E2942;">
                    <p style="font-size: 16px; font-weight: 800;"><b>⚡ Status:</b> Pontuação salva no Ranking!</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

        with c_quote:
            st.markdown(
                """
                <div style="padding: 40px; text-align: center;">
                    <blockquote style="font-size: 22px; font-style: italic; color: #FFC107; font-weight: 900;">
                        "Conhecer o passado é entender o presente e construir o futuro."
                    </blockquote>
                </div>
            """,
                unsafe_allow_html=True,
            )

        st.write("")
        if st.button("VOLTAR PARA OS JOGOS ➔"):
            st.session_state.tela = "grade_jogos"
            st.rerun()

# --- TELA: RANKING REAL (ESTritamente LIMPO) ---
elif st.session_state.tela == "ranking":
    st.subheader("🏆 RANKING GERAL (JOGADORES REAIS)")
    st.caption("Classificação real baseada exclusivamente nos jogadores cadastrados:")

    if len(db["jogadores"]) == 0:
        st.info("Ainda não existem perfis registados. Cadastre o seu perfil na aba de Login e seja o primeiro do ranking!")
    else:
        jogadores_ordenados = sorted(
            db["jogadores"].items(), key=lambda x: x[1]["xp"], reverse=True
        )

        tabela_ranking = []
        for pos, (username, dados) in enumerate(jogadores_ordenados, start=1):
            medalha = (
                "🥇 1º"
                if pos == 1
                else (
                    "🥈 2º"
                    if pos == 2
                    else ("🥉 3º" if pos == 3 else f"⭐ {pos}º")
                )
            )

            ic_avatar = "📷" if dados.get("foto_base64") else dados.get("avatar", "🎓")

            tabela_ranking.append(
                {
                    "Posição": medalha,
                    "Estudante": f"{ic_avatar} {dados['nome_exibicao']}",
                    "XP Total": f"{dados['xp']} XP",
                    "Moedas": f"🪙 {dados['moedas']}",
                    "Acertos": f"✅ {dados['acertos']}",
                }
            )

        st.table(tabela_ranking)

# --- TELA: CONQUISTAS ---
elif st.session_state.tela == "conquistas":
    st.subheader("🎖️ SUAS CONQUISTAS E INSÍGNIAS")
    st.caption("Evolua nos seus estudos para desbloquear novas insígnias:")

    if st.session_state.usuario_atual and st.session_state.usuario_atual in db["jogadores"]:
        u = db["jogadores"][st.session_state.usuario_atual]
        acertos_user = u["acertos"]
        xp_user = u["xp"]
    else:
        acertos_user = 0
        xp_user = 0

    c1, c2, c3 = st.columns(3)

    with c1:
        if acertos_user >= 1:
            st.success("⭐ Primeiro Passo\n\nConcluiu o primeiro desafio com acerto!")
        else:
            st.info("🔒 Primeiro Passo\n\nResponda a 1 desafio corretamente.")

    with c2:
        if acertos_user >= 5:
            st.success("🧠 Mente Histórica\n\nAlcançou 5 acertos acumulados!")
        else:
            st.info(f"🔒 Mente Histórica\n\nProgresso: {acertos_user}/5 acertos.")

    with c3:
        if xp_user >= 500:
            st.success("🏆 Mestre do ENEM\n\nAcumulou mais de 500 XP!")
        else:
            st.info(f"🔒 Mestre do ENEM\n\nProgresso: {xp_user}/500 XP.")

# --- TELA: PERFIL DO JOGADOR ---
elif st.session_state.tela == "perfil":
    st.subheader("👤 SEU PERFIL DE JOGADOR")

    if not st.session_state.usuario_atual or st.session_state.usuario_atual not in db["jogadores"]:
        st.warning("Efetue o login para visualizar as suas estatísticas.")
        if st.button("Ir para Login"):
            st.session_state.tela = "login"
            st.rerun()
    else:
        u = db["jogadores"][st.session_state.usuario_atual]

        col_p1, col_p2 = st.columns([1, 2])

        with col_p1:
            st.markdown(
                f"""
                <div style="background-color: #0F1526; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #1E2942;">
            """,
                unsafe_allow_html=True,
            )

            if u.get("foto_base64"):
                st.markdown(
                    f'<img src="data:image/png;base64,{u["foto_base64"]}" style="width:130px; height:130px; border-radius:50%; object-fit:cover; border:3px solid #FFC107;">',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div style="font-size: 70px;">{u.get("avatar", "🎓")}</div>',
                    unsafe_allow_html=True,
                )

            st.markdown(
                f"""
                    <h2 style="color: #FFC107; margin-bottom: 5px; font-weight: 900;">{u['nome_exibicao']}</h2>
                    <p style="color: #8D99AE; font-size: 14px; font-weight: 800;">@{st.session_state.usuario_atual}</p>
                    <p style="font-style: italic; font-weight: 800;">"{u['bio']}"</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

        with col_p2:
            st.markdown("### 📊 Desempenho Estatístico Real")

            total_res = u["acertos"] + u["erros"]
            taxa = (u["acertos"] / total_res * 100) if total_res > 0 else 0

            st.write(f"⚡ **XP Total:** {u['xp']}")
            st.write(f"🪙 **Moedas:** {u['moedas']}")
            st.write(f"✅ **Acertos:** {u['acertos']}")
            st.write(f"❌ **Erros:** {u['erros']}")
            st.write(f"🎯 **Precisão Geral:** {taxa:.1f}%")

            st.markdown("---")
            st.markdown("### ✏️ Editar Dados e Foto de Perfil")
            novo_nome_e = st.text_input("Nome de Exibição:", value=u["nome_exibicao"])
            nova_bio_e = st.text_input("Frase / Meta de Estudo:", value=u["bio"])
            
            st.write("**Carregar nova foto da Galeria do seu dispositivo:**")
            foto_upload_e = st.file_uploader("Escolher foto da galeria:", type=["png", "jpg", "jpeg"], key="upload_perfil_edit")

            if st.button("💾 SALVAR ALTERAÇÕES DO PERFIL"):
                u["nome_exibicao"] = novo_nome_e
                u["bio"] = nova_bio_e
                
                if foto_upload_e is not None:
                    foto_bytes_e = foto_upload_e.read()
                    u["foto_base64"] = base64.b64encode(foto_bytes_e).decode("utf-8")
                
                salvar_banco_dados(db)
                st.success("Perfil atualizado com sucesso!")
                st.rerun()