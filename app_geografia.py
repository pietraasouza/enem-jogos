import base64
import json
import os
import streamlit as st

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E ESTILIZAÇÃO CSS (GEOGRAFIA GAME - NEON & OCEANO)
# ==============================================================================
st.set_page_config(
    page_title="Geografia Game Studio — Explore o Mundo",
    page_icon="🌍",
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
        background: linear-gradient(90deg, #0A1C38 0%, #0F1526 100%);
        padding: 18px 28px;
        border-radius: 18px;
        border: 2px solid #0088FF;
        margin-bottom: 25px;
        box-shadow: 0 4px 25px rgba(0, 136, 255, 0.25);
    }
    
    .status-badge {
        background-color: #121D38;
        padding: 8px 18px;
        border-radius: 25px;
        font-weight: 900 !important;
        color: #00E676;
        border: 2px solid #00E676;
        font-size: 15px;
    }

    /* Cartões dos Modos */
    .card-modo-normal {
        background: linear-gradient(180deg, #0A2647 0%, #061021 100%);
        border: 3px solid #0088FF;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 136, 255, 0.3);
    }
    
    .card-modo-desafio {
        background: linear-gradient(180deg, #3A0CA3 0%, #17032B 100%);
        border: 3px solid #7209B7;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 25px rgba(114, 9, 183, 0.4);
    }

    .card-modo-simulado {
        background: linear-gradient(180deg, #093325 0%, #03140E 100%);
        border: 3px solid #00E676;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 25px rgba(0, 230, 118, 0.3);
    }

    /* Caixa da Questão */
    .question-box {
        background-color: #0F1526;
        border: 2px solid #0088FF;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        font-weight: 800 !important;
    }

    /* Dica Teórica */
    .dica-box {
        background-color: #112240;
        color: #64FFDA;
        padding: 18px 22px;
        border-radius: 14px;
        font-weight: 900 !important;
        font-size: 15px;
        margin-bottom: 20px;
        border-left: 8px solid #64FFDA;
        box-shadow: 0 4px 15px rgba(100, 255, 218, 0.15);
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
        background: linear-gradient(180deg, #0088FF 0%, #0055CC 100%) !important;
        color: #FFFFFF !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 14px 28px !important;
        font-size: 16px !important;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(0, 136, 255, 0.4);
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0, 136, 255, 0.6);
    }

    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        font-weight: 800 !important;
        border-radius: 12px !important;
        background-color: #0F1526 !important;
        color: #FFFFFF !important;
        border: 2px solid #0088FF !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. BANCO DE DADOS LOCAL (100% LIMPO - APENAS JOGADORES REAIS)
# ==============================================================================
DB_FILE = "banco_geografia_jogadores.json"


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
if "modo_jogo" not in st.session_state:
    st.session_state.modo_jogo = "Normal"
if "desafio_id" not in st.session_state:
    st.session_state.desafio_id = 0
if "fase_jogo" not in st.session_state:
    st.session_state.fase_jogo = "pergunta"
if "continente_selecionado" not in st.session_state:
    st.session_state.continente_selecionado = "América do Sul"

# ==============================================================================
# 4. ESTRUTURA DO MODO EXPLORAÇÃO (EXPEDIÇÃO PELO PLANETA)
# ==============================================================================
CONTINENTES_EXPLORACAO = {
    "América do Sul": {
        "icone": "🏔️",
        "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800",
        "missoes": [
            {
                "id_m": "as_1",
                "titulo": "O Mistério da Amazônia",
                "tempo": "2 min",
                "pergunta": "Qual fator contribui diretamente para a grande vazão e relevância da Bacia Amazônica?",
                "opcoes": [
                    "Predomínio de clima desértico",
                    "Extensa rede hidrográfica pluvial e grande disponibilidade de água",
                    "Ausência de vegetação natural",
                    "Predomínio de rios temporários"
                ],
                "correta": "Extensa rede hidrográfica pluvial e grande disponibilidade de água",
                "resumo_diario": "📘 **Bacia Amazônica:** Maior bacia hidrográfica do planeta, com regime predominantemente pluvial e grande papel na regulação do clima global.",
                "xp": 50,
                "moedas": 20
            }
        ]
    },
    "África": {
        "icone": "🌍",
        "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800",
        "missoes": [
            {
                "id_m": "af_1",
                "titulo": "O Desafio do Sahel",
                "tempo": "2 min",
                "pergunta": "O Sahel é uma faixa de transição no continente africano que sofre gravemente com qual processo?",
                "opcoes": [
                    "Desertificação e pressão antrópica",
                    "Glaciação intensa",
                    "Arenização por clima temperado",
                    "Tsunamis recorrentes"
                ],
                "correta": "Desertificação e pressão antrópica",
                "resumo_diario": "📘 **Sahel Africano:** Faixa semiárida vulnerável ao avanço da desertificação devido ao uso intensivo do solo e mudanças climáticas.",
                "xp": 50,
                "moedas": 20
            }
        ]
    },
    "Ásia": {
        "icone": "⛩️",
        "img": "https://images.unsplash.com/photo-1508804039946-6428a5957777?w=800",
        "missoes": [
            {
                "id_m": "as_2",
                "titulo": "Zonas Econômicas Chinesas",
                "tempo": "2 min",
                "pergunta": "Qual modelo impulsionou a rápida atração de indústrias e capitais para o litoral da China?",
                "opcoes": [
                    "Zonas Econômicas Especiais (ZEEs)",
                    "Isolamento comercial absoluto",
                    "Feudalismo de subsistência",
                    "Econômica voltada apenas para o mercado interno"
                ],
                "correta": "Zonas Econômicas Especiais (ZEEs)",
                "resumo_diario": "📘 **China e ZEEs:** Abertura econômica ao capital estrangeiro no litoral, mantendo o controle político do Estado.",
                "xp": 50,
                "moedas": 20
            }
        ]
    },
    "Europa": {
        "icone": "🏰",
        "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800",
        "missoes": [
            {
                "id_m": "eu_1",
                "titulo": "A Transição Demográfica Europeia",
                "tempo": "2 min",
                "pergunta": "Qual a principal característica do perfil populacional da Europa Ocidental atualmente?",
                "opcoes": [
                    "Envelhecimento populacional e baixa taxa de fecundidade",
                    "Explosão demográfica jovem",
                    "Elevada taxa de mortalidade infantil",
                    "Migração massiva de saída"
                ],
                "correta": "Envelhecimento populacional e baixa taxa de fecundidade",
                "resumo_diario": "📘 **Demografia Europeia:** Desafio da previdência e necessidade de atração de mão de obra imigrante qualificada.",
                "xp": 50,
                "moedas": 20
            }
        ]
    }
}

# ==============================================================================
# 5. BASE DE DADOS DOS 30 DESAFIOS (15 FÍSICA + 15 HUMANA - MATRIZ ENEM)
# ==============================================================================
DESAFIOS_GEOGRAFIA = [
    # --- GEOGRAFIA FÍSICA (1 a 15) ---
    {
        "id": 1,
        "categoria": "Geografia Física",
        "nome": "1. Clima",
        "sub": "Arenização x Desertificação",
        "dica": "💡 DICA ENEM: A arenização ocorre em solos arenosos com clima úmido (ex: Pampa gaúcho), enquanto a desertificação afeta regiões áridas e semiáridas (ex: Caatinga).",
        "pergunta": "No sudoeste do Rio Grande do Sul, o manejo inadequado do solo arenoso aliado ao pisoteio do gado tem provocado a exposição do lençol freático e a formação de grandes manchas de areia. Qual processo ambiental caracteriza essa degradação específica?",
        "opcoes": ["Arenização", "Desertificação", "Salinização do solo", "Lateralização profunda"],
        "correta": "Arenização",
        "explicacao": "A arenização ocorre no bioma Pampa devido à dinâmica hídrica e solos arenosos vulneráveis.",
        "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800"
    },
    {
        "id": 2,
        "categoria": "Geografia Física",
        "nome": "2. Relevo",
        "sub": "Anamorfose Cartográfica",
        "dica": "💡 DICA ENEM: A anamorfose distorce a forma física dos países para proporcionalizar a área cartografada ao valor do dado estatístico representado.",
        "pergunta": "Ao analisar um mapa-múndi em que o continente africano e a América Latina aparecem desproporcionalmente gigantescos em relação à Europa e América do Norte, constata-se que o dado representado reflete:",
        "opcoes": [
            "Exportação de commodities agrícolas ou participação na pegada ecológica",
            "Consumo global de energia elétrica per capita",
            "Investimento em patentes de alta tecnologia",
            "Concentração de sedes de empresas multinacionais"
        ],
        "correta": "Exportação de commodities agrícolas ou participação na pegada ecológica",
        "explicacao": "A anamorfose ajusta o tamanho territorial à variável estatística analisada.",
        "img": "https://images.unsplash.com/photo-1524661135-423995f22d0b?w=800"
    },
    {
        "id": 3,
        "categoria": "Geografia Física",
        "nome": "3. Hidrografia",
        "sub": "Movimentos de Massa",
        "dica": "💡 DICA ENEM: A remoção da cobertura vegetal nas encostas aumenta a infiltração de água no solo (saturação), desencadeando deslizamentos no verão.",
        "pergunta": "Nas metrópoles tropicais brasileiras, os episódios recorrentes de escorregamento de terra em morros habitados durante os meses de chuva intensa resultam da combinação entre:",
        "opcoes": [
            "Pluviometria elevada e ocupação desordenada de áreas de risco",
            "Sismos de baixa magnitude e erosão eólica acelerada",
            "Movimentos tectônicos convergentes na Serra do Mar",
            "Aumento da taxa de evapotranspiração das florestas urbanas"
        ],
        "correta": "Pluviometria elevada e ocupação desordenada de áreas de risco",
        "explicacao": "O fator humano potencializa o risco geológico durante as tempestades.",
        "img": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=800"
    },
    {
        "id": 4,
        "categoria": "Geografia Física",
        "nome": "4. Vegetação",
        "sub": "O Cerrado e o Agronegócio",
        "dica": "💡 DICA ENEM: O Cerrado é considerado o 'berço das águas' do Brasil, mas sofre com a conversão de sua vegetação nativa em monoculturas de soja e pastagens.",
        "pergunta": "A expansão da fronteira agrícola na região conhecida como MATOPIBA (Maranhão, Tocantins, Piauí e Bahia) afeta diretamente qual domínio morfoclimático brasileiro?",
        "opcoes": ["Cerrado", "Caatinga", "Mata dos Cocais", "Domínio das Araucárias"],
        "correta": "Cerrado",
        "explicacao": "O MATOPIBA representa a principal área de avanço do agronegócio sobre o Cerrado.",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800"
    },
    {
        "id": 5,
        "categoria": "Geografia Física",
        "nome": "5. Solos",
        "sub": "Ilhas de Calor Urbanas",
        "dica": "💡 DICA ENEM: Materiais escuros (asfalto, concreto) e pouca arborização retêm calor no centro das cidades, elevando a temperatura local.",
        "pergunta": "Qual intervenção urbanística é mais eficaz para mitigar o efeito microclimático da 'ilha de calor' nas grandes centralidades urbanas?",
        "opcoes": [
            "Criação de parques lineares e telhados verdes",
            "Asfaltamento completo das vias secundárias",
            "Aumento da densidade de edifícios espelhados",
            "Canalização fechada dos rios e córregos urbanos"
        ],
        "correta": "Criação de parques lineares e telhados verdes",
        "explicacao": "A vegetação aumenta a evapotranspiração e reduz a absorção de radiação solar.",
        "img": "https://images.unsplash.com/photo-1477959858617-67f30bc75b82?w=800"
    },
    {
        "id": 6,
        "categoria": "Geografia Física",
        "nome": "6. Biomas",
        "sub": "Transição Energética Global",
        "dica": "💡 DICA ENEM: A busca pela descarbonização da economia visa cumprir as metas do Acordo de Paris.",
        "pergunta": "A substituição progressiva dos combustíveis fósseis por fontes eólicas, solares e biomassa enfrenta como obstáculo geopolítico principal:",
        "opcoes": [
            "A dependência econômica de países exportadores de petróleo e o custo de armazenamento da energia",
            "A total indisponibilidade de tecnologia eólica nos países em desenvolvimento",
            "A rejeição popular generalizada ao uso de painéis fotovoltaicos",
            "A ausência de radiação solar suficiente na faixa intertropical"
        ],
        "correta": "A dependência econômica de países exportadores de petróleo e o custo de armazenamento da energia",
        "explicacao": "Resistências econômicas e desafios técnicos de intermitência atrasam a transição.",
        "img": "https://images.unsplash.com/photo-1509391365360-2e959784a276?w=800"
    },
    {
        "id": 7,
        "categoria": "Geografia Física",
        "nome": "7. Recursos Naturais",
        "sub": "Bônus Demográfico",
        "dica": "💡 DICA ENEM: O bônus demográfico ocorre quando a proporção de pessoas em idade ativa (PIA) é maior que a de dependentes.",
        "pergunta": "Para aproveitar plenamente a fase do 'bônus demográfico' antes do envelhecimento acelerado da população, o Estado deve priorizar investimentos em:",
        "opcoes": [
            "Educação de qualidade, capacitação técnica e geração de empregos formais",
            "Redução sistemática das vagas no ensino superior público",
            "Incentivo exclusivo à emigração de jovens qualificados",
            "Aumento da idade mínima de escolarização obrigatória"
        ],
        "correta": "Educação de qualidade, capacitação técnica e geração de empregos formais",
        "explicacao": "A PIA qualificada gera riqueza e sustenta o sistema de previdência social.",
        "img": "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=800"
    },
    {
        "id": 8,
        "categoria": "Geografia Física",
        "nome": "8. Cartografia",
        "sub": "Grilagem de Terras",
        "dica": "💡 DICA ENEM: A concentração fundiária histórica no Brasil gera tensões socioambientais frequentes nas regiões de fronteira agrícola.",
        "pergunta": "O conceito de 'grilagem de terras', frequentemente debatido na Geografia Agrária brasileira, refere-se a:",
        "opcoes": [
            "Falsificação de documentos para apropriação ilegal de terras públicas",
            "Técnica biológica de controle de pragas na lavoura de milho",
            "Processo de reflorestamento obrigatório em áreas de preservação",
            "Arrendamento legal de propriedades rurais para agricultura familiar"
        ],
        "correta": "Falsificação de documentos para apropriação ilegal de terras públicas",
        "explicacao": "Grilagem é a posse ilícita de terras por meio da fraude de títulos.",
        "img": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=800"
    },
    {
        "id": 9,
        "categoria": "Geografia Física",
        "nome": "9. Geologia",
        "sub": "Gentrificação Urbana",
        "dica": "💡 DICA ENEM: Gentrificação é a valorização imobiliária de bairros centrais que expulsa a população de baixa renda.",
        "pergunta": "Qual consequência socioespacial é associada aos projetos de revitalização urbana conhecidos como 'gentrificação'?",
        "opcoes": [
            "Segregação socioespacial e encarecimento do custo de vida local",
            "Democratização imediata do acesso à moradia digna para todos",
            "Redução da especulação imobiliária nas áreas centrais",
            "Descentralização total do comércio para as zonas rurais"
        ],
        "correta": "Segregação socioespacial e encarecimento do custo de vida local",
        "explicacao": "A chegada de serviços de alto padrão eleva aluguéis e expulsa moradores antigos.",
        "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800"
    },
    {
        "id": 10,
        "categoria": "Geografia Física",
        "nome": "10. Desastres Naturais",
        "sub": "Transposição do Rio São Francisco",
        "dica": "💡 DICA ENEM: A transposição visa garantir oferta de água para bacias secundárias do Semiárido brasileiro.",
        "pergunta": "O objetivo socioeconômico central da obra de transposição das águas do Rio São Francisco é:",
        "opcoes": [
            "Mitigar a vulnerabilidade hídrica de populações e atividades produtivas no Semiárido",
            "Gerar eletricidade para a Região Sul do Brasil",
            "Inundar permanentemente a vegetação da Caatinga",
            "Permitir a navegação de grandes navios cargueiros transatlânticos"
        ],
        "correta": "Mitigar a vulnerabilidade hídrica de populações e atividades produtivas no Semiárido",
        "explicacao": "Os eixos levam água potável a reservatórios de regiões afetadas pela seca.",
        "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800"
    },
    {
        "id": 11,
        "categoria": "Geografia Física",
        "nome": "11. População",
        "sub": "Meio Técnico-Informacional",
        "dica": "💡 DICA ENEM: Conceito de Milton Santos que define a fase atual onde ciência e tecnologia orientam o espaço.",
        "pergunta": "O meio técnico-científico-informacional manifesta-se no espaço geográfico por meio de:",
        "opcoes": [
            "Infraestruturas digitais, redes de fibra óptica e fluxos instantâneos de capital",
            "Uso exclusivo da tração animal nas lavouras e vilas isoladas",
            "Predomínio da extração mineral sem automação",
            "Substituição das cidades por comunidades autossuficientes isoladas"
        ],
        "correta": "Infraestruturas digitais, redes de fibra óptica e fluxos instantâneos de capital",
        "explicacao": "As redes de informação interligam nós estratégicos da economia em tempo real.",
        "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800"
    },
    {
        "id": 12,
        "categoria": "Geografia Física",
        "nome": "12. Urbanização",
        "sub": "Estruturas Geológicas do Brasil",
        "dica": "💡 DICA ENEM: Bacias sedimentares abrigam combustíveis fósseis, enquanto escudos cristalinos possuem minerais metálicos.",
        "pergunta": "A Província Mineral de Carajás (PA) e o Quadrilátero Ferrífero (MG) estão associados a qual estrutura geológica do território brasileiro?",
        "opcoes": [
            "Escudos Cristalinos (Crátons) do Pré-Cambriano",
            "Bacias Sedimentares do Cenozoico",
            "Dobramentos Modernos do Terciário",
            "Fossas Oceânicas profundas"
        ],
        "correta": "Escudos Cristalinos (Crátons) do Pré-Cambriano",
        "explicacao": "As rochas antigas dos escudos cristalinos concentram grandes jazidas minerais metálicas.",
        "img": "https://images.unsplash.com/photo-1579912437766-789233630f0f?w=800"
    },
    {
        "id": 13,
        "categoria": "Geografia Física",
        "nome": "13. Economia",
        "sub": "A Nova Rota da Seda",
        "dica": "💡 DICA ENEM: O projeto chinês busca expandir a influência comercial e infraestrutural global.",
        "pergunta": "Qual o principal objetivo estratégico da China ao financiar ferrovias, portos e gasodutos no projeto da 'Nova Rota da Seda'?",
        "opcoes": [
            "Assegurar rotas de escoamento de seus produtos e garantir acesso a matérias-primas energéticas",
            "Doar recursos financeiros sem exigência de contrapartidas econômicas",
            "Promover a isolação total do comércio marítimo internacional",
            "Transferir toda a sua população urbana para países vizinhos"
        ],
        "correta": "Assegurar rotas de escoamento de seus produtos e garantir acesso a matérias-primas energéticas",
        "explicacao": "A China consolida corredores logísticos globais sob seu controle estratégico.",
        "img": "https://images.unsplash.com/photo-1508804039946-6428a5957777?w=800"
    },
    {
        "id": 14,
        "categoria": "Geografia Física",
        "nome": "14. Globalização",
        "sub": "Estatuto do Refugiado",
        "dica": "💡 DICA ENEM: O refugiado cruza fronteiras por perseguição, guerras ou violações graves de direitos humanos.",
        "pergunta": "Segundo a Convenção de 1951 da ONU, a condição jurídica de 'refugiado' é concedida a indivíduos que:",
        "opcoes": [
            "Fugiram de seus países devido a conflitos armados ou perseguição política, étnica ou religiosa",
            "Se mudaram voluntariamente para estudar ou trabalhar no exterior",
            "Viajam temporariamente a trabalho como executivos de multinacionais",
            "Compraram imóveis em outros países para investimento financeiro"
        ],
        "correta": "Fugiram de seus países devido a conflitos armados ou perseguição política, étnica ou religiosa",
        "explicacao": "O refúgio é uma proteção internacional obrigatória baseada em direitos humanos.",
        "img": "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=800"
    },
    {
        "id": 15,
        "categoria": "Geografia Física",
        "nome": "15. Geopolítica",
        "sub": "Hotspots de Biodiversidade",
        "dica": "💡 DICA ENEM: Hotspots são áreas com altíssima biodiversidade endêmica e mais de 70% de degradação original.",
        "pergunta": "Quais são os dois biomas brasileiros classificados internacionalmente como 'Hotspots' de biodiversidade?",
        "opcoes": ["Mata Atlântica e Cerrado", "Amazônia e Caatinga", "Pampa e Pantanal", "Mata de Araucárias e Manguezais"],
        "correta": "Mata Atlântica e Cerrado",
        "explicacao": "Ambos possuem riqueza biológica endêmica e sofrem intensa pressão antrópica histórica.",
        "img": "https://images.unsplash.com/photo-1448375240586-882707db888b?w=800"
    },

    # --- GEOGRAFIA HUMANA E REGIONAL (16 a 30) ---
    {
        "id": 16,
        "categoria": "Geografia Humana",
        "nome": "16. América Latina",
        "sub": "Industrialização Tardia",
        "dica": "💡 DICA ENEM: A industrialização da América Latina ocorreu por Substituição de Importações no século XX.",
        "pergunta": "Qual foi o modelo econômico adotado pelo Brasil e México no século XX para impulsionar suas indústrias nacionais?",
        "opcoes": [
            "Industrialização por Substituição de Importações (ISI)",
            "Capitalismo agrário de livre mercado absoluto",
            "Coletivismo agrário estrito",
            "Filtração de capitais exclusivamente externos"
        ],
        "correta": "Industrialização por Substituição de Importações (ISI)",
        "explicacao": "Com as crises mundiais, os países passaram a fabricar internamente o que antes importavam.",
        "img": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800"
    },
    {
        "id": 17,
        "categoria": "Geografia Humana",
        "nome": "17. África",
        "sub": "Fronteiras Artificiais",
        "dica": "💡 DICA ENEM: As fronteiras africanas traçadas na Conferência de Berlim uniram etnias rivais e dividiram povos.",
        "pergunta": "Qual foi a consequência geopolítica principal da imposição de fronteiras arbitrárias pelos europeus na África?",
        "opcoes": [
            "Guerras civis étnicas crônicas e instabilidade política duradoura",
            "Desenvolvimento industrial autônomo imediato",
            "Unificação cultural pacífica de todo o continente",
            "Eliminação total da pobreza extrema"
        ],
        "correta": "Guerras civis étnicas crônicas e instabilidade política duradoura",
        "explicacao": "O desrespeito às nações locais gerou conflitos profundos após a descolonização.",
        "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800"
    },
    {
        "id": 18,
        "categoria": "Geografia Humana",
        "nome": "18. Ásia",
        "sub": "Socialismo de Mercado",
        "dica": "💡 DICA ENEM: A China combinou o controle político do Partido Comunista com abertura econômica capitalista.",
        "pergunta": "Qual modelo econômico transformou a China em potência global a partir de 1978?",
        "opcoes": [
            "Socialismo de Mercado (Zonas Econômicas Especiais)",
            "Feudalismo agrário tecnológico",
            "Capitalismo liberal sem controle estatal",
            "Economia voltada apenas para consumo interno"
        ],
        "correta": "Socialismo de Mercado (Zonas Econômicas Especiais)",
        "explicacao": "A abertura econômica em zonas litorâneas atraiu investimentos estrangeiros massivos.",
        "img": "https://images.unsplash.com/photo-1508804039946-6428a5957777?w=800"
    },
    {
        "id": 19,
        "categoria": "Geografia Humana",
        "nome": "19. Europa",
        "sub": "Envelhecimento Demográfico",
        "dica": "💡 DICA ENEM: A Europa enfrenta um desafio demográfico severo com baixas taxas de fecundidade.",
        "pergunta": "Qual é o principal impacto econômico do envelhecimento demográfico acelerado na Europa Ocidental?",
        "opcoes": [
            "Pressão sobre a previdência social e necessidade de atração de imigrantes",
            "Excesso absoluto de mão de obra jovem desempregada",
            "Colapso imediato da agricultura familiar",
            "Fim do setor de alta tecnologia"
        ],
        "correta": "Pressão sobre a previdência social e necessidade de atração de imigrantes",
        "explicacao": "Com menos trabalhadores ativos por aposentado, os governos dependem da imigração.",
        "img": "https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800"
    },
    {
        "id": 20,
        "categoria": "Geografia Humana",
        "nome": "20. Oceania",
        "sub": "Mudanças Climáticas Insulares",
        "dica": "💡 DICA ENEM: Pequenos Estados insulares do Pacífico sofrem diretamente com a elevação do nível do mar.",
        "pergunta": "Qual é a principal ameaça ambiental enfrentada pelos pequenos Estados insulares do Oceano Pacífico?",
        "opcoes": [
            "Elevação do nível médio dos oceanos devido ao aquecimento global",
            "Desertificação extrema por desmatamento interno",
            "Vulcanismo generalizado e contínuo",
            "Terremotos diários de magnitude 9"
        ],
        "correta": "Elevação do nível médio dos oceanos devido ao aquecimento global",
        "explicacao": "Por serem ilhas de baixa altitude, correm risco severo de submersão.",
        "img": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800"
    },
    {
        "id": 21,
        "categoria": "Geografia Humana",
        "nome": "21. Brasil",
        "sub": "Hierarquia Urbana",
        "dica": "💡 DICA ENEM: A rede urbana brasileira é highly centralizada, tendo São Paulo como metrópole nacional máxima.",
        "pergunta": "O que caracteriza uma Metrópole Nacional na hierarquia urbana brasileira?",
        "opcoes": [
            "Área de influência que abrange todo o território nacional com serviços e sedes de grandes empresas",
            "Cidade de pequeno porte com economia estritamente agrícola",
            "Capital estadual sem conexão com outras regiões",
            "Centro urbano isolado sem infraestrutura digital"
        ],
        "correta": "Área de influência que abrange todo o território nacional com serviços e sedes de grandes empresas",
        "explicacao": "São Paulo comanda a economia e a rede de transportes e telecomunicações do país.",
        "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800"
    },
    {
        "id": 22,
        "categoria": "Geografia Humana",
        "nome": "22. Espaço Geográfico",
        "sub": "Território e Poder",
        "dica": "💡 DICA ENEM: Para a geografia crítica, o território envolve relações de poder e soberania sobre o espaço.",
        "pergunta": "Na acepção da geografia crítica, o que diferencia 'Território' de 'Espaço Geográfico'?",
        "opcoes": [
            "O território envolve relações de poder, soberania e apropriação política de um espaço",
            "O território é apenas a natureza selvagem sem interferência humana",
            "O espaço geográfico não possui intervenção da sociedade",
            "O território é sinônimo exclusivo de clima"
        ],
        "correta": "O território envolve relações de poder, soberania e apropriação política de um espaço",
        "explicacao": "O território é delimitado por fronteiras e relações de domínio político ou econômico.",
        "img": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800"
    },
    {
        "id": 23,
        "categoria": "Geografia Humana",
        "nome": "23. Meio Ambiente",
        "sub": "Conferências Ambientais da ONU",
        "dica": "💡 DICA ENEM: A Eco-92 consolidou o conceito de Desenvolvimento Sustentável globalmente.",
        "pergunta": "Qual protocolo internacional histórico estabeleceu metas obrigatórias de redução de emissão de gases de efeito estufa?",
        "opcoes": ["Protocolo de Quioto", "Acordo de Paris", "Conferência de Estocolmo", "Carta da Terra"],
        "correta": "Protocolo de Quioto",
        "explicacao": "Assinado em 1997, Quioto impôs metas legais aos países desenvolvidos.",
        "img": "https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=800"
    },
    {
        "id": 24,
        "categoria": "Geografia Humana",
        "nome": "24. Desenvolvimento Sustentável",
        "sub": "Tripé da Sustentabilidade",
        "dica": "💡 DICA ENEM: O desenvolvimento sustentável apoia-se no tripé ambiental, social e econômico.",
        "pergunta": "Qual pilar NÃO faz parte dos três eixos fundamentais da sustentabilidade?",
        "opcoes": ["Pilar estritamente militar", "Pilar ambiental", "Pilar econômico", "Pilar social"],
        "correta": "Pilar estritamente militar",
        "explicacao": "A sustentabilidade foca no equilíbrio ambiental, social e viabilidade econômica.",
        "img": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?w=800"
    },
    {
        "id": 25,
        "categoria": "Geografia Humana",
        "nome": "25. Território e Fronteiras",
        "sub": "Cidades Gêmeas",
        "dica": "💡 DICA ENEM: As fronteiras modernas funcionam como zonas de intensa integração e troca cultural.",
        "pergunta": "O que caracteriza uma fronteira viva ou faixa de fronteira em termos geopolíticos?",
        "opcoes": [
            "Área de integração e intercâmbio cultural e comercial intenso entre países vizinhos",
            "Muro intransponível que impede qualquer tipo de contato humano",
            "Região desabitada sem nenhuma legislação aplicada",
            "Espaço marítimo internacional livre de leis"
        ],
        "correta": "Área de integração e intercâmbio cultural e comercial intenso entre países vizinhos",
        "explicacao": "As cidades gêmeas nas fronteiras partilham comércio, serviços e cotidiano social.",
        "img": "https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?w=800"
    },
    {
        "id": 26,
        "categoria": "Geografia Humana",
        "nome": "26. Migrações",
        "sub": "Fatores de Repulsão (Push Factors)",
        "dica": "💡 DICA ENEM: Guerras, desemprego e pobreza atuam como fatores de repulsão nos fluxos migratórios.",
        "pergunta": "Qual fator econômico e social atua classicamente como 'repulsão' nos fluxos migratórios?",
        "opcoes": ["Desemprego crônico, guerras civis e pobreza extrema", "Oferta abundante de empregos bem remunerados", "Estabilidade política e paz social", "Excelentes serviços públicos de saúde"],
        "correta": "Desemprego crônico, guerras civis e pobreza extrema",
        "explicacao": "Fatores de repulsão forçam as pessoas a deixarem suas pátrias em busca de sobrevivência.",
        "img": "https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=800"
    },
    {
        "id": 27,
        "categoria": "Geografia Humana",
        "nome": "27. Conflitos e Tensões",
        "sub": "Oriente Médio e Recursos Hídricos",
        "dica": "💡 DICA ENEM: A disputa por territórios e água na bacia dos rios Jordão e Eufrates agrava os conflitos regionais.",
        "pergunta": "Qual fator histórico e territorial está no centro do conflito israelo-palestino?",
        "opcoes": ["A disputa pela posse de terras ancestrais e soberania em Jerusalém", "A exploração exclusiva de minas de ouro na Antártida", "A divisão de fronteiras comerciais na América Central", "A soberania sobre o Canal do Panamá"],
        "correta": "A disputa pela posse de terras ancestrais e soberania em Jerusalém",
        "explicacao": "A partilha da terra e o direito de retorno de refugiados são questões geopolíticas centrais.",
        "img": "https://images.unsplash.com/photo-1579912437766-789233630f0f?w=800"
    },
    {
        "id": 28,
        "categoria": "Geografia Humana",
        "nome": "28. Cultura e Diversidade",
        "sub": "A Aldeia Global",
        "dica": "💡 DICA ENEM: Conceito que expressa a encolha do mundo em termos de comunicação em tempo real.",
        "pergunta": "O que significa o conceito de 'Aldeia Global' na geografia da comunicação?",
        "opcoes": ["A interconexão instantânea de informações e culturas no planeta via redes globais", "O isolamento total de vilarejos rurais sem tecnologia", "A eliminação de todas as línguas locais do mundo", "A padronização agrícola de sementes transgênicas"],
        "correta": "A interconexão instantânea de informações e culturas no planeta via redes globais",
        "explicacao": "Indica que as redes de telecomunicação conectam o planeta instantaneamente.",
        "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800"
    },
    {
        "id": 29,
        "categoria": "Geografia Humana",
        "nome": "29. Agronegócio",
        "sub": "Modernização Agrícola",
        "dica": "💡 DICA ENEM: O agronegócio exportador brasileiro baseia-se em alta tecnologia, mecanização e sementes selecionadas.",
        "pergunta": "O que caracteriza a agricultura patronal moderna (Agronegócio exportador)?",
        "opcoes": ["Elevado uso de tecnologia, maquinário avançado, sementes selecionadas e foco na exportação", "Uso exclusivo de tração animal e ferramentas manuais rudimentares", "Policultura voltada unicamente para a subsistência familiar local", "Ausência total de crédito bancário e adubos químicos"],
        "correta": "Elevado uso de tecnologia, maquinário avançado, sementes selecionadas e foco na exportação",
        "explicacao": "O agronegócio moderno é highly capitalizado e integrado ao mercado global.",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=800"
    },
    {
        "id": 30,
        "categoria": "Geografia Humana",
        "nome": "30. Geografia do Brasil",
        "sub": "Complexos Regionais do IBGE",
        "dica": "💡 DICA ENEM: A divisão regional do IBGE baseia-se em critérios físico-naturais e socioeconômicos.",
        "pergunta": "Qual região brasileira concentra a maior parte da população urbana e o principal parque industrial do país?",
        "opcoes": ["Região Sudeste", "Região Norte", "Região Centro-Oeste", "Região Sul"],
        "correta": "Região Sudeste",
        "explicacao": "O Sudeste lidera a densidade demográfica, o PIB industrial e o setor financeiro nacional.",
        "img": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800"
    }
]

# ==============================================================================
# 6. BARRA SUPERIOR DINÂMICA
# ==============================================================================
if st.session_state.usuario_atual and st.session_state.usuario_atual in db["jogadores"]:
    u = db["jogadores"][st.session_state.usuario_atual]
    xp_val = u["xp"]
    moedas_val = u["moedas"]
    ofensiva_val = u["ofensiva"]
    nome_exib = u["nome_exibicao"]
    avatar_exib = "📷" if u.get("foto_base64") else u.get("avatar", "🌍")
else:
    xp_val = 0
    moedas_val = 0
    ofensiva_val = 0
    nome_exib = "Sem Perfil Ativo"
    avatar_exib = "👤"

st.markdown(
    f"""
    <div class="top-bar">
        <div style="font-size: 20px; font-weight: 900; color: #00E676;">
            {avatar_exib} {nome_exib.upper()}
        </div>
        <div>
            <span class="status-badge">🔥 {ofensiva_val} DIAS</span>
            <span class="status-badge" style="margin-left: 10px; color: #FFC107; border-color: #FFC107;">🪙 {moedas_val}</span>
            <span class="status-badge" style="margin-left: 10px;">⚡ {xp_val} XP</span>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# Menu Superior de Navegação
m1, m2, m3, m4, m5, m6 = st.columns(6)
if m1.button("🏠 INÍCIO"):
    st.session_state.tela = "inicio"
    st.rerun()
if m2.button("🧭 EXPLORAÇÃO"):
    if st.session_state.usuario_atual:
        st.session_state.tela = "modo_exploracao"
    else:
        st.session_state.tela = "login"
    st.rerun()
if m3.button("🎮 JOGOS"):
    if st.session_state.usuario_atual:
        st.session_state.tela = "desafios_lista"
    else:
        st.session_state.tela = "login"
    st.rerun()
if m4.button("🏆 RANKING"):
    st.session_state.tela = "ranking"
    st.rerun()
if m5.button("🎖️ CONQUISTAS"):
    st.session_state.tela = "conquistas"
    st.rerun()
if m6.button("👤 PERFIL"):
    if st.session_state.usuario_atual:
        st.session_state.tela = "perfil"
    else:
        st.session_state.tela = "login"
    st.rerun()

st.markdown("---")

# ==============================================================================
# 7. GERENCIADOR DE TELAS E FLUXO COMPLETO DO JOGO
# ==============================================================================

# --- TELA: LOGIN E CADASTRO SEGURO (PRIVACIDADE TOTAL) ---
if st.session_state.tela == "login":
    st.subheader("🔑 CRIAR PERFIL OU ENTRAR NO GEOGRAFIA GAME")
    st.caption("Digite o seu username privado para entrar ou crie uma nova conta na aba ao lado!")

    tab_login, tab_cadastro = st.tabs(["Entrar na Minha Conta", "Criar Novo Perfil Real"])

    with tab_login:
        st.write("Digite o seu username cadastrado para aceder:")
        nick_input = st.text_input("O seu Username de Acesso:").strip().lower()
        
        if st.button("🚀 ENTRAR NA MINHA CONTA"):
            if not nick_input:
                st.error("Por favor, digite o seu username!")
            elif nick_input in db["jogadores"]:
                st.session_state.usuario_atual = nick_input
                st.success(f"Bem-vindo de volta, {db['jogadores'][nick_input]['nome_exibicao']}!")
                st.session_state.tela = "inicio"
                st.rerun()
            else:
                st.error("Username não encontrado! Verifique se digitou corretamente ou crie um novo perfil na aba ao lado.")

    with tab_cadastro:
        novo_username = st.text_input("Escolha um Username único (ex: ana_geo):").strip().lower()
        novo_nome = st.text_input("Seu Nome de Exibição:")
        nova_bio = st.text_input("Sua Meta de Estudo:", value="Explorador do Planeta Terra!")
        
        novo_avatar = st.selectbox("Escolha um Ícone de Avatar:", ["🌍", "🧭", "🌋", "🏔️", "🌊", "🚀", "🛰️"])
        
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
                    "diario": []
                }
                salvar_banco_dados(db)
                st.session_state.usuario_atual = novo_username
                st.success("Perfil registado com sucesso!")
                st.session_state.tela = "inicio"
                st.rerun()

# --- TELA: INÍCIO (EXPLORE O MUNDO) ---
elif st.session_state.tela == "inicio":
    col_banner, col_info = st.columns([2, 1])

    with col_banner:
        st.markdown(
            """
            <div style="background: linear-gradient(90deg, #0A1C38 0%, #12264A 100%); padding: 40px; border-radius: 20px; border: 2px solid #0088FF;">
                <h1 style="color: #00E676; font-size: 40px; margin-bottom: 0;">🌍 EXPLORE O MUNDO</h1>
                <p style="color: #8D99AE; font-size: 16px; font-weight: 800;">E CONQUISTE O SEU FUTURO NO ENEM</p>
                <p style="margin-top: 15px; font-size: 16px;"><b>30 desafios estilo ENEM</b> + Modo Exploração com mapa dos continentes e diário de estudo!</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        c_b1, c_b2 = st.columns(2)
        if c_b1.button("🧭 MODO EXPLORAÇÃO"):
            if st.session_state.usuario_atual:
                st.session_state.tela = "modo_exploracao"
            else:
                st.session_state.tela = "login"
            st.rerun()
        if c_b2.button("🎮 JOGOS E SIMULADO"):
            if st.session_state.usuario_atual:
                st.session_state.tela = "modos_jogo"
            else:
                st.session_state.tela = "login"
            st.rerun()

    with col_info:
        st.markdown(
            """
            <div style="background-color: #0F1526; padding: 25px; border-radius: 20px; border: 2px solid #0088FF;">
                <h3 style="color: #00E676; margin-top: 0;">💡 Dica Geográfica</h3>
                <p style="font-size: 15px; font-weight: 800;">"A geografia é a chave para entender o mundo e o seu lugar nele." Explore os continentes e domine a física e a humana!</p>
            </div>
        """,
            unsafe_allow_html=True,
        )

# --- TELA: MODO EXPLORAÇÃO (MAPA INTERATIVO DOS CONTINENTES) ---
elif st.session_state.tela == "modo_exploracao":
    st.subheader("🧭 MODO EXPLORAÇÃO: EXPEDIÇÃO PELO PLANETA")
    st.caption("Aventure-se pelos continentes, cumpra missões no estilo ENEM e preencha o seu Diário do Explorador!")

    cols = st.columns(2)
    idx_col = 0

    for cont_nome, cont_dados in CONTINENTES_EXPLORACAO.items():
        with cols[idx_col % 2]:
            st.markdown(
                f"""
                <div style="background-color: #0F1526; border: 2px solid #0088FF; padding: 20px; border-radius: 18px; margin-bottom: 15px;">
                    <h3 style="color: #00E676; margin-top:0;">{cont_dados['icone']} {cont_nome}</h3>
                    <p style="font-size: 13px; font-weight:800; color: #8D99AE;">Missões de Expedição: {len(cont_dados['missoes'])}</p>
                </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button(f"EXPLORAR {cont_nome.upper()}", key=f"btn_exp_{cont_nome}"):
                st.session_state.continente_selecionado = cont_nome
                st.session_state.tela = "missoes_continente"
                st.rerun()

        idx_col += 1

# --- TELA: MISSÕES DO CONTINENTE SELECIONADO ---
elif st.session_state.tela == "missoes_continente":
    cont_nome = st.session_state.continente_selecionado
    cont_dados = CONTINENTES_EXPLORACAO[cont_nome]

    st.subheader(f"{cont_dados['icone']} EXPEDIÇÃO: {cont_nome.upper()}")
    st.caption("Complete as missões para desbloquear recompensas e registos no seu Diário de Estudo!")

    if len(cont_dados["missoes"]) == 0:
        st.info("Novas missões estão a ser mapeadas para esta região!")
    else:
        for mis in cont_dados["missoes"]:
            c_m1, c_m2 = st.columns([2, 1])
            with c_m1:
                st.markdown(
                    f"""
                    <div style="background-color: #0F1526; border: 2px solid #00E676; padding: 20px; border-radius: 16px; margin-bottom: 15px;">
                        <h3 style="color: #00E676; margin-top:0;">{mis['titulo']}</h3>
                        <p style="font-size: 15px; font-weight: 800;">{mis['pergunta']}</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                for opt in mis["opcoes"]:
                    if st.button(opt, key=f"btn_m_opt_{opt}"):
                        if st.session_state.usuario_atual in db["jogadores"]:
                            u = db["jogadores"][st.session_state.usuario_atual]
                            if opt == mis["correta"]:
                                u["xp"] += mis["xp"]
                                u["moedas"] += mis["moedas"]
                                if "diario" not in u:
                                    u["diario"] = []
                                if mis["resumo_diario"] not in u["diario"]:
                                    u["diario"].append(mis["resumo_diario"])
                                salvar_banco_dados(db)
                                st.success(f"✅ Missão Concluída! +{mis['xp']} XP | +{mis['moedas']} Moedas acumuladas e resumo adicionado ao seu Diário!")
                            else:
                                st.error("❌ Resposta incorreta! Tente novamente para libertar o conhecimento.")

            with c_m2:
                st.image(cont_dados["img"], use_container_width=True)

# --- TELA: ESCOLHA DO MODO DE JOGO ---
elif st.session_state.tela == "modos_jogo":
    st.subheader("🎮 ESCOLHA O MODO DE JOGO")
    st.caption("Selecione como deseja encarar os desafios de geografia:")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            """
            <div class="card-modo-normal">
                <h2>NORMAL</h2>
                <h3 style="color: #0088FF; font-size: 22px;">Ritmo Próprio</h3>
                <p style="font-weight: 800;">Questões no seu ritmo. Ideal para aprender e fixar os conceitos com calma.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("JOGAR NORMAL"):
            st.session_state.modo_jogo = "Normal"
            st.session_state.tela = "desafios_lista"
            st.rerun()

    with c2:
        st.markdown(
            """
            <div class="card-modo-desafio">
                <h2>DESAFIO</h2>
                <h3 style="color: #7209B7; font-size: 22px;">Modo Pressão</h3>
                <p style="font-weight: 800;">Mais pontos, mais emoção. Mantenha a sequência correta e multiplique seus bônus!</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("JOGAR DESAFIO"):
            st.session_state.modo_jogo = "Desafio"
            st.session_state.tela = "desafios_lista"
            st.rerun()

    with c3:
        st.markdown(
            """
            <div class="card-modo-simulado">
                <h2>SIMULADO ENEM</h2>
                <h3 style="color: #00E676; font-size: 22px;">Estilo Oficial</h3>
                <p style="font-weight: 800;">Questões altamente contextualizadas com textos, gráficos, mapas e análises críticas.</p>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("JOGAR SIMULADO"):
            st.session_state.modo_jogo = "Simulado ENEM"
            st.session_state.tela = "desafios_lista"
            st.rerun()

# --- TELA: GRADE DOS 30 DESAFIOS (FÍSICA & HUMANA) ---
elif st.session_state.tela == "desafios_lista":
    st.subheader(f"🌐 OS 30 DESAFIOS DE GEOGRAFIA — MODO: {st.session_state.modo_jogo.upper()}")
    st.caption("15 Desafios de Geografia Física | 15 Desafios de Geografia Humana (Matriz ENEM)")

    tab_fisica, tab_humana = st.tabs(["⚡ GEOGRAFIA FÍSICA (1-15)", "🌍 GEOGRAFIA HUMANA (16-30)"])

    with tab_fisica:
        for row in range(3):
            cols = st.columns(5)
            for col_idx in range(5):
                idx = row * 5 + col_idx  # 0 a 14
                if idx < len(DESAFIOS_GEOGRAFIA):
                    desafio = DESAFIOS_GEOGRAFIA[idx]
                    with cols[col_idx]:
                        st.markdown(
                            f"""
                            <div style="background-color: #0F1526; border: 2px solid #0088FF; padding: 18px; border-radius: 16px; text-align: center;">
                                <div style="font-size: 22px;">🏔️</div>
                                <small style="font-size: 11px; font-weight: 800;"><b>{desafio['nome']}</b></small><br>
                                <span style="color: #00E676; font-size: 10px; font-weight: 900;">⭐ LIBERADO</span>
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )
                        st.write("")
                        if st.button("JOGAR", key=f"btn_fis_{idx}"):
                            st.session_state.desafio_id = idx
                            st.session_state.tela = "gameplay"
                            st.session_state.fase_jogo = "pergunta"
                            st.rerun()

    with tab_humana:
        for row in range(3):
            cols = st.columns(5)
            for col_idx in range(5):
                idx = 15 + (row * 5 + col_idx)  # 15 a 29
                if idx < len(DESAFIOS_GEOGRAFIA):
                    desafio = DESAFIOS_GEOGRAFIA[idx]
                    with cols[col_idx]:
                        st.markdown(
                            f"""
                            <div style="background-color: #0F1526; border: 2px solid #00E676; padding: 18px; border-radius: 16px; text-align: center;">
                                <div style="font-size: 22px;">🏙️</div>
                                <small style="font-size: 11px; font-weight: 800;"><b>{desafio['nome']}</b></small><br>
                                <span style="color: #00E676; font-size: 10px; font-weight: 900;">⭐ LIBERADO</span>
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )
                        st.write("")
                        if st.button("JOGAR", key=f"btn_hum_{idx}"):
                            st.session_state.desafio_id = idx
                            st.session_state.tela = "gameplay"
                            st.session_state.fase_jogo = "pergunta"
                            st.rerun()

# --- TELA: GAMEPLAY INTERATIVA ---
elif st.session_state.tela == "gameplay":
    desafio = DESAFIOS_GEOGRAFIA[st.session_state.desafio_id]

    if st.session_state.fase_jogo == "pergunta":
        st.subheader(f"DESAFIO {desafio['id']}: {desafio['nome'].upper()} | {desafio['sub']}")

        col_img, col_q = st.columns([1, 1.2])

        with col_img:
            st.image(desafio["img"], use_container_width=True)
            st.markdown(
                f"<div class='dica-box'>{desafio['dica']}</div>",
                unsafe_allow_html=True,
            )

        with col_q:
            st.markdown(
                f"""
                <div class="question-box">
                    <h3 style="margin-top: 0; font-weight: 900;">{desafio['pergunta']}</h3>
                </div>
            """,
                unsafe_allow_html=True,
            )

            for opt in desafio["opcoes"]:
                if st.button(opt, key=f"btn_opt_val_{opt}"):
                    if st.session_state.usuario_atual in db["jogadores"]:
                        u = db["jogadores"][st.session_state.usuario_atual]
                        if opt == desafio["correta"]:
                            u["xp"] += 150
                            u["moedas"] += 50
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
                <h1 style="color: #00E676; font-size: 45px; margin-top: 0;">✅ ACERTOU!</h1>
                <p style="font-size: 17px; font-weight: 800;">{desafio['explicacao']}</p>
                <br>
                <div style="font-size: 20px; font-weight: 900; color: #FFC107;">
                    ⚡ + 150 XP &nbsp;&nbsp;&nbsp;&nbsp; 🪙 + 50 MOEDAS
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("AVANÇAR E CONCLUIR ➔"):
            st.session_state.fase_jogo = "fim"
            st.rerun()

    # --- TELA ERROU ---
    elif st.session_state.fase_jogo == "errou":
        st.markdown(
            f"""
            <div class="error-card">
                <h1 style="color: #FF3366; font-size: 45px; margin-top: 0;">❌ RESPOSTA INCORRETA</h1>
                <p style="font-size: 17px; font-weight: 800;">Por que as outras estão erradas? Revise o conceito:</p>
                <div style="background-color: #24050C; padding: 20px; border-radius: 14px; border: 2px solid #FF3366; color: #FFFFFF; font-weight: 800;">
                    {desafio['dica']}
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("🔄 TENTAR NOVAMENTE"):
            st.session_state.fase_jogo = "pergunta"
            st.rerun()

    # --- TELA FIM DO DESAFIO ---
    elif st.session_state.fase_jogo == "fim":
        st.balloons()
        c_res, c_quote = st.columns(2)

        with c_res:
            st.markdown(
                """
                <div style="background-color: #0F1526; padding: 35px; border-radius: 20px; text-align: center; border: 2px solid #0088FF;">
                    <h2 style="color: #00E676; margin-top: 0;">🏆 DESAFIO GEOGRÁFICO CONCLUÍDO!</h2>
                    <h1 style="color: #00E676; font-size: 55px;">100%</h1>
                    <p style="color: #8D99AE; font-weight: 800;">Sua pontuação foi gravada com sucesso no seu perfil oficial!</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

        with c_quote:
            st.markdown(
                """
                <div style="padding: 40px; text-align: center;">
                    <blockquote style="font-size: 22px; font-style: italic; color: #00E676; font-weight: 900;">
                        "Grandes conquistas são feitas de pequenos avanços geográficos."
                    </blockquote>
                </div>
            """,
                unsafe_allow_html=True,
            )

        st.write("")
        if st.button("VOLTAR PARA OS DESAFIOS ➔"):
            st.session_state.tela = "desafios_lista"
            st.rerun()

# --- TELA: RANKING REAL (ESTRITAMENTE LIMPO) ---
elif st.session_state.tela == "ranking":
    st.subheader("🏆 RANKING GERAL (JOGADORES REAIS)")
    st.caption("Classificação baseada estritamente no XP obtido por quem se cadastrou:")

    if len(db["jogadores"]) == 0:
        st.info("Ainda não existem utilizadores registados. Cadastre o seu perfil na aba de Login e seja o primeiro do ranking!")
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

            ic_avatar = "📷" if dados.get("foto_base64") else dados.get("avatar", "🌍")

            tabela_ranking.append(
                {
                    "Posição": medalha,
                    "Explorador": f"{ic_avatar} {dados['nome_exibicao']}",
                    "XP Total": f"{dados['xp']} XP",
                    "Moedas": f"🪙 {dados['moedas']}",
                    "Desafios Concluídos": f"✅ {dados['jogos_concluidos']}",
                }
            )

        st.table(tabela_ranking)

# --- TELA: CONQUISTAS ---
elif st.session_state.tela == "conquistas":
    st.subheader("🎖️ SUAS CONQUISTAS E INSÍGNIAS")
    st.caption("Desbloqueie títulos geográficos conforme evolui nos estudos:")

    if st.session_state.usuario_atual and st.session_state.usuario_atual in db["jogadores"]:
        u = db["jogadores"][st.session_state.usuario_atual]
        concluidos = u["jogos_concluidos"]
        xp_user = u["xp"]
    else:
        concluidos = 0
        xp_user = 0

    c1, c2, c3 = st.columns(3)

    with c1:
        if concluidos >= 1:
            st.success("⭐ Primeiro Acerto\n\nConcluiu o primeiro desafio geográfico!")
        else:
            st.info("🔒 Primeiro Acerto\n\nComplete 1 desafio.")

    with c2:
        if concluidos >= 10:
            st.success("🗺️ Mestre dos Mapas\n\nCompletou 10 desafios de geografia!")
        else:
            st.info(f"🔒 Mestre dos Mapas\n\nProgresso: {concluidos}/10.")

    with c3:
        if xp_user >= 1000:
            st.success("🌍 Geógrafo ENEM\n\nUltrapassou 1000 XP acumulados!")
        else:
            st.info(f"🔒 Geógrafo ENEM\n\nProgresso: {xp_user}/1000 XP.")

# --- TELA: PERFIL COM DIÁRIO DO EXPLORADOR E UPLOAD DA GALERIA ---
elif st.session_state.tela == "perfil":
    st.subheader("👤 SEU PERFIL DE EXPLORADOR")

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
                <div style="background-color: #0F1526; padding: 30px; border-radius: 20px; text-align: center; border: 2px solid #0088FF;">
            """,
                unsafe_allow_html=True,
            )

            if u.get("foto_base64"):
                st.markdown(
                    f'<img src="data:image/png;base64,{u["foto_base64"]}" style="width:130px; height:130px; border-radius:50%; object-fit:cover; border:3px solid #00E676;">',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div style="font-size: 70px;">{u.get("avatar", "🌍")}</div>',
                    unsafe_allow_html=True,
                )

            st.markdown(
                f"""
                    <h2 style="color: #00E676; margin-bottom: 5px; font-weight: 900;">{u['nome_exibicao']}</h2>
                    <p style="color: #8D99AE; font-size: 14px; font-weight: 800;">@{st.session_state.usuario_atual}</p>
                    <p style="font-style: italic; font-weight: 800;">"{u['bio']}"</p>
                </div>
            """,
                unsafe_allow_html=True,
            )

        with col_p2:
            st.markdown("### 📊 Painel de Desempenho Geográfico")

            total_res = u["acertos"] + u["erros"]
            taxa = (u["acertos"] / total_res * 100) if total_res > 0 else 0

            st.write(f"⚡ **XP Total:** {u['xp']}")
            st.write(f"🪙 **Moedas:** {u['moedas']}")
            st.write(f"✅ **Desafios Concluídos:** {u['jogos_concluidos']}")
            st.write(f"🎯 **Precisão Geral:** {taxa:.1f}%")

            st.markdown("---")
            st.markdown("### 📖 Diário do Explorador (Anotações de Estudo para o ENEM)")
            
            if "diario" in u and len(u["diario"]) > 0:
                for resumo in u["diario"]:
                    st.info(resumo)
            else:
                st.caption("Ainda não possui anotações no diário. Complete missões no Modo Exploração para desbloquear resumos automáticos de revisão!")

            st.markdown("---")
            st.markdown("### ✏️ Editar Perfil e Foto da Galeria")
            novo_nome_e = st.text_input("Nome de Exibição:", value=u["nome_exibicao"])
            nova_bio_e = st.text_input("Meta de Estudo:", value=u["bio"])
            
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