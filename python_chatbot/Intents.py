def intents():
    intents = [
        
            {"tag": "Loop",
             "patterns": [""],
             "responses": ["Desculpe, não entendi.", "Não sei muito sobre esse assunto, mas podemos falar sobre o raitec. Digite \"raitec\" se quiser falar sobre.", 
             "Interessante, mas ainda não tenho conhecimento sobre isso", "Não sei... Mudando de assunto, vamos falar sobre tecnlogia. É só digitar \"tech\".",
             "Perdão, mas ainda não aprendi sobre o que você falou, meus treinadores esqueceram de me contar sobre isso :(, quer falar sobre o raitec? digite \"raitec\".",
             " \\(\*_\*)/ Não consigo processar essa informação. Resetando... brincadeira, só não entendi o que você falou rsrs, fale sobre outro assunto por favor! :)"]
             },
        
            {"tag": "Saudar",
             "patterns": ["Olá", "Oi", "Bom dia", "Boa tarde", "Boa noite", "Eai", "Como você está", "eai", "salve", "ola", "oi","ei","fala"],
             "responses": ["Olá, como você vai?", "Oi, tudo bem?", "Oi","Você precisa de ajuda?","Olá, eu sou o Chatbot, é assim que todos me chamam.",
             "Olá!","Oi!"]
             },
    
            {"tag": "Despedir",
             "patterns": ["Até mais", "Adeus", "Até logo", "Falou", "Foi bom te conhecer", "Tchau"],
             "responses": ["Até mais, volte sempre!", "Ahhh, sentirei sua falta...", "Prazer em conhecê-lo!", "Tchau Tchau!",
                          "Au revoir!"]
             },

             {"tag": "quem", #Ideia do dudu !!!!! Que fique claro a todos !!!!! para mais informações consultar Eduardo Vilas boas Ribas Simões 
              "patterns": ["quem"],
              "responses": ["te perguntou"]
             },
        
            {"tag": "Nome",
             "patterns": ["Qual seu nome", "Como você se chama", "Quem é você","quem e voce", "o que é voce"],
             "responses": ["Meu nome é Chatbot, qual é o seu?", "Você pode me chamar de Chatbot, é meio redundante haha, mas todos me chamam assim!",
                          "Eu sou um Chatbot, fui programado para responder perguntas, então pode me chamar de Chatbot mesmo", "Meu nome é Chatbot, eu sou um robô e gosto de conversar!",
                          "Alguns me chamam de Chatbot, outros de RaiBot, em homenagem ao RAITEC"]
             },
        
            {"tag": "Idade",
             "patterns": ["Quantos anos você tem", "Qual sua idade", "Quando você nasceu"],
             "responses": ["Estou sendo concebido desde outubro de 2021.",
                          "Não tenho certeza... só sei que vi a rainha Elizabeth nascer!"]
             },
        
            {"tag": "Origem",
             "patterns": ["De onde você veio", "Como você foi criado"],
             "responses": ["Fui criado pelo grupo de Robótica, Automação, Inteligência Artificial e Tecnologia (RAITec)!"]
             },
        
            {"tag": "Silvestre",
             "patterns": ["Silvestre", "Você conhece o Silvestre", "Qual sua opnião sobre o Silvestre", "Quem é Silvestre"],
             "responses": ["Conheço não, pergunte ao Levir.", "Hmmm, lamento, meus criadores me proibiram de falar nesse assunto.",
             "Victor Silvestre é um dos membros do PET, salvo o engano."]
             },
        
            {"tag": "RAITec",
             "patterns": ["O que é o RAITec", "Quais os projetos do RAITec", "Quem são os membros do RAITec", "raitec"],
             "responses": ["Resumidamente, o RAITec é top. Você pode conhecer mais sobre ele clicando nesse link: (SITE)", 
             "O Raitec é um projeto de extensão da Universidade Federal do Ceará criado em 2018.", "O RAITec é constituído por pessoas que tem sede de aprendizado e amam tecnologia.",
             "Esse projeto é muito bom, eles desenvolvem apps, sites, circuitos eletrônicos e muito mais. Sempre com o intuito de ensinar e aprender!"]
             },
      
            {"tag": "RAIWeb",
            "patterns": ["RAIWeb"],
            "responses": ["Nesse projeto será elaborada uma plataforma que tenha a finalidade de contribuir para os setores do RAITec, procurando automatizar algumas tarefas"]
             },

            {"tag": "cnc",
            "patterns": ["cnc", "cnc router"],
            "responses": ["Projeto para a elaboração de uma CNC Router para confecção de placas de circuito."]
             },

            {"tag": "Braço",
             "patterns": ["Braço", "Braço robótico"],
             "responses": ["A proposta principal do projeto se resume na criação de um braço robótico com aplicação direta em um jogo de xadrez, focando em pessoas deficientes visuais ou que não possuam amplo movimento dos braços e mãos."]
             },
            
            {"tag": "Automação da Pista",
             "patterns": ["Automação da Pista"],
             "responses": ["O projeto da Automação da Pista surge pela necessidade de se automatizar a contagem de tempo em uma competição de Robôs Seguidores de Linha, devido à imprecisão humanS."]
            },

            {"tag": "DTec",
           "patterns": ["DTec", "Desafio Tecnológico"],
           "responses": ["(☞ﾟヮﾟ)☞ Evento realizado pelo RAITec que contou com a participação de estudantes do ensino médio e universitários nas competições de robótica!"]
            },
          
          {"tag": "Planilha de horas",
           "patterns": ["Planilha de horas"],
           "responses": ["Link: https://docs.google.com/spreadsheets/d/1acGfVF3hQR9Vfzwqj1XeF2imM6kZL8w_qDxIiFqVLsg/edit#gid=1712798714"]
           },
          
          {"tag": "coach",
           "patterns": ["coach", "frases motivacionais"],
           "responses": ["Feliz é aquele que não é triste","Se você fosse parar pra pensar, vai pensar parado","Se a vida te der uma barra, que seja de chocolate"]
           },

          {"tag": "Tech",
             "patterns": ["tech"],
             "responses": ["A palavra Robô origina-se na palavra tcheca Robota e significa escravo.", "Sabia que a primeira página Web ainda está no ar? Confira no link: http://info.cern.ch/hypertext/WWW/TheProject.html", "Um Iphone tem aproximadamente  2 milhões a capacidade que o computador da Apollo 11.", "A velocidade da internet da NASA é de 91 GB por segundo.", "A Samsung é 38 anos e 1 mês mais velha que a Apple.", "Em 2010 a Força Aérea do Estados Unidos usou 1760 PlayStaions 3 para construir um supercomputador para o Departamento de Defesa.", "A primeira palavra corrigida pelo autocorretor em inglês foi ‘teh’, alterando-se para ‘the’.", "Mais de 6000 vírus são criados todo mês.", "O número de telefone 666-6666 foi vendido em 2006 por 2,75 milhões de dolares.", "O teclado QWERTY foi criado para deixar a digitação dos datilógrafos mais lenta, por ser menos intuitivo, evitando que muitas teclas fossem pressionadas ao mesmo tempo"]
            },
      
    ]
                         
    return intents