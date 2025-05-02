import segno, segno.helpers

#Função para criar QrCode para um website
def site():
    #O usuário deve entrar com a Url do web site
    site=input("Digite o site para criar o QrCode: ")
    #O usuário deve fornecer o nome para cirar a imagem em png
    nome=input("Digite o nome que desejas nomear o QrCode: ")
    #O segno cria o qr code com as informações dada, podendo mudar as cores do fundo (campo "light")
    #ou os blocos (campo "Dark") e o tamanho (campo "scale")
    QrSite = segno.make(site)
    QrSite.save(nome+'.png', dark="black", light="white", scale=10)

#Função para criar QrCode para uma rede Wifi
def wifi():
    #O usuário deve fornecer o nome da rede wifi
    ssid=input("Digite o nome da sua rede wifi: ")
    #O usuário deve fornecer a senha da rede
    password=input("Digite a senha da sua rede wifi: ")
    #O usuário deve fornecer um nome para o QrCode que sera criado
    nome=input("Digite o nome que desejas nomear o QrCode: ")
    #As informações são setadas para o segno 
    wifi_settings = {
        'ssid':str(ssid), 
        'password':str(password), 
        'security': str('WPA2-PSK')
        }

    wifi = segno.helpers.make_wifi(**wifi_settings)

    #O segno cria o qr code com as informações dada, podendo mudar as cores do fundo (campo "light")
    #ou os blocos (campo "Dark") e o tamanho (campo "scale")
    wifi.save(nome+".png", dark="black", light="white", scale=10)
#O usuário deve digitar uma das opções
print("Bem vindo! Para começar selecione opção de QrCode desejas criar. (1 ,2 ou 3)")
tipo=int(input("\n1:Wifi"
        "\n2:Site"
        "\n3:Finalizar o programa\n"
        "\nOpção: "))
#Loop de repetição para o programa continuar rodando enquanto não for selecionado a opção 3
while tipo!=3:
    #Se a opção selecionada for 1 a função wifi sera usada
    if (tipo==1):
        wifi()
        #O usuário poderá escolher outra opção ou finalizar o programa
        print("QrCode criado na pasta do programa\n"
        "\nSe quiser continue use uma das opções. (1 , 2 ou 3)")
        tipo=int(input("\n1:Wifi"
        "\n2:Site"
        "\n3:Finalizar o programa\n"
        "\nOpção: "))
    elif tipo==2:
        #Se a opção selecionada for 2 a função site sera usada
        site()
        #O usuário poderá escolher outra opção ou finalizar o programa
        print("QrCode criado na pasta do programa"
        "\nSe quiser continuar use uma das opções. (1 , 2 ou 3)")
        tipo=int(input("\n1:Wifi"
        "\n2:Site"
        "\n3:Finalizar o programa\n"
        "\nOpção: "))
    else:
        #No caso de uma opção diferente o usuário terá uma informação de que foi inválido a seleção
        #Nesse caso ele poderá selecionar outra opção
        print("Opção inválida! Use uma das opções abaixo. (1, 2 ou 3)")
        tipo=int(input("\n1:Wifi"
        "\n2:Site"
        "\n3:Finalizar o programa\n"
        "\nOpção: "))