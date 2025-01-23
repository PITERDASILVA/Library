class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False
    
    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return True
        return False
    
    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponivel"
        return f"{self.titulo} - {self.autor} ({self.ano}) [{status}]"
    
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro_(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca")
        for i, livro in enumerate(self.livros, 1):
            print (f"{i}. {livro}")

    def emprestar_livro(self,titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.emprestar():
                    print (f"O livro '{titulo}' foi emprestado.")
                    return
                else:
                    print (f"O livro '{titulo}' foi já está emprestado.")
                    return
            print(f"O livro '{titulo}' não foi encontrado.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.devolver():
                    print(f"O livro '{titulo}' foi devolvido.")
                    return
                else: 
                     print(f"O livro '{titulo}' já está disponível.")
                     return
            print(f"O livro '{titulo}' não foi encontrado.")




def exibir_menu():
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()  
        
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção:")
            

        if escolha == '1':
            titulo = input("Digite o titulo do Livro: ")
            autor = input("Digite o autor do Livro: ")
            ano = input("Digite o ano do Livro: ")
            livro = Livro(titulo, autor, ano)
            biblioteca.adicionar_livro_(livro)
            print(f"O livro '{titulo}' foi adicionado com sucesso.")

        elif escolha == '2':
            biblioteca.listar_livros()

        elif escolha == '3':
            titulo = input("Digite o titulo do Livro:")
            biblioteca.emprestar_livro(titulo)

        elif escolha == '4': 
            titulo = input("Digite o titulo do Livro:")
            biblioteca.devolver_livro(titulo)

        elif escolha == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()  
    
   