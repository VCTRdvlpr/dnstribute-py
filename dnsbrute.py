import dns.resolver # modulo da biblioteca 'dnspython' usado para realizar consultas DNS 

res = dns.resolver.Resolver()  # criando uma instância da classe Resolver do módulo dns.resolver. Isso permitirá realizar consultas DNS usando as configurações padrão do sistema
arquivo = open("/home/kali/wordlist.txt", "r") # usando um arquivo "wordlist.txt" localizado no diretório "/home/kali/" em modo de leitura ("r"), o arquivo contém diversos possíveis nomes de subdominios. 
subdominios = arquivo.read().splitlines() # lendo o conteúdo do arquivo usando o método 'read()' e dividindo o conteúdo em linhas usando 'splitlines()'. Isso resultará em uma lista chamada 'subdominios' que conterá cada linha do arquivo como um elemento da lista.

alvo = "exemplo.com.br" #  define a variável alvo. Este é o dominio principal, que será concatenado com os subdomínios da lista.

for subdominio in subdominios: # Aqui começa o loop for para cada subdominio na lista 'subdominios', construindo o nome completo do subdomínio ao concatenar o domínio principal com os subdomínios. 
	try:    # Dentro do bloco try, está sendo usada a instância do resolvedor res para fazer uma consulta DNS usando o método resolve(sub_alvo, "A")          
		sub_alvo = subdominio + "." + alvo  # Isso buscará o endereço IP (registro A) associado ao subdomínio. Se a consulta for bem-sucedida, você entra em um loop 'for' que itera sobre os resultados (endereços IP) e imprime o subdomínio completo e o endereço IP.
		resultado = res.resolve(sub_alvo, "A")
		for ip in resultado:
			print(sub_alvo, "->", ip)
	except:
		pass  # Se ocorrer uma exceção (qualquer erro) durante o processo de consulta ou resolução DNS, o bloco except irá capturá-la e o código continuará executando de forma silenciosa devido ao uso de pass

# O ARQUIVO 'wordlist.txt' DEVERÁ SER ALTERADO, POIS ESTE É UM ARQUIVO SALVO EM UM DIRETÓRIO LOCAL
# NO MEU COMPUTADOR, PORÉM É UM ARQUIVO DE TEXTO SIMPLES CRIADO EM UM BLOCO DE NOTAS COM POSSÍVEIS NOMES
# DE SUBDOMINIOS EXISTENTES ( user, admin, etc). O UNICO PONTO DE ATENÇÃO É QUE OS NOMES DEVERÃO ESTAR LISTADOS UM
# EM CADA LINHA, POIS O SCRIPT IRA LER O ARQUIVO DESTA FORMA    