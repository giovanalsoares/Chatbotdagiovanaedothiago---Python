import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r'oi|ola|olá|eai|e aí|boa noite|bom dia|boa tarde',
        ['Olá. Como vai?', 'Oi. Como vai?', 'Hey. Como vai?',]  
    ],
    [
        r'tudo bem|tudo certo|vou bem|bem|estou bem|tô bem|to bem',
        ['Que bom! :) Esse é o chatbot da lanchonete da Giovana e do Thiago. Você gostaria de consultar o nosso cardápio?',]
    ],
    [
        r'mal|nao muito bem|n vou bem|triste|cansado|cansada|chateada|chateado|nada bem|não estou bem|não to bem|n estou bem',
        ['Que pena :( Esse é o chatbot da lanchonete da Giovana e do Thiago. Você gostaria de consultar o nosso cardápio para alegrar o seu dia com uma lanche?',]
    ],
    [
        r'sim|por favor|s|pode ser|aham|ok|cardápio',
        ['1: X-tudo, 2: X-Bacon, 3: X-Vegan, 4: Cachorrão. Para a confirmação do seu pedido só é necessário nos informar o número do seu pedido. Exemplo: se você deseja o "cachorrão", você só precisa responder com "4"!',]
    ],
    [
        r'1|2|3|4|batata',
        ['Ótima escolha! Gostaria de batata frita grande, média, pequena ou nenhuma?',]
    ],
    [
        r'grande|Grande|média|Média|pequena|Pequena|g|G|m|M|p|P|nenhuma|nada|nao|Nao|n|N|não|Não|pagamento',
        ['Qual será a forma de pagamento: cartão de crédito/débito ou dinheiro?']
    ],
    [
        r'crédito|credito|débito|debito|cartão|cartão de crédito|cartão de débito|dinheiro|à vista',
        ['Ok. Pedido feito. Obrigada pela preferência e até a próxima :)',]
    ],
    [
        r'até|Até|inté|obrigada|té|ate',
        [':)',]
    ],
    [
        r'(.*)',
        ['%1? Desculpe, ainda não sei a resposta para isso :(. Digite a palavra "cardápio" caso você tenha tido dúvida com o cardápio, assim como, "pagamento"/"batata" para dúvidas referentes a essas etapas :)',]
    ],
]

        
def chatbotgiovanaethiago():
    print ('Olá! Esse é o chatbot da Giovana e do Thiago.')
    chat = Chat (pairs, reflections)
    chat.converse ()
    
if __name__ == '__main__':
    chatbotgiovanaethiago ()
