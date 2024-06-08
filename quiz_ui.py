import tkinter as tk
import random
from tkinter import ttk
from PIL import Image, ImageTk
from quiz_logic import QuizLogic

class QuizUI:
    def __init__(self, master, logic):
        self.logic = logic
        self.master = master
        self.master.title("Quiz de Filmes")
        self.master.geometry("1200x700")
        self.master.configure(bg="#2c2c2c")
        self.master.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat",
                             background="#004d40", foreground="#ffffff", font=("Comic Sans MS", 12))
        self.style.map("TButton",
                       foreground=[('pressed', 'white'), ('active', 'white')],
                       background=[('pressed', '#003d33'), ('active', '#003d33')])
        self.style.configure("TLabel", background="#2c2c2c", font=("Comic Sans MS", 14), foreground="#ffffff")
        self.style.configure("TFrame", background="#2c2c2c")

        self.detalhes_visiveis = False

        self.frame_inicial = ttk.Frame(master)
        self.frame_inicial.pack(expand=True)

        self.label_inicial = tk.Label(self.frame_inicial, text="Bem-vindo ao Quiz de Filmes", bg="#2c2c2c", fg="white", font=("Comic Sans MS", 24, "bold"))
        self.label_inicial.pack(pady=20)

        self.btn_iniciar = tk.Button(self.frame_inicial, text="Iniciar Quiz", command=self.iniciar_quiz,
                                     bg="#00796b", fg="white", font=("Comic Sans MS", 14), relief="flat", width=20, height=2)
        self.btn_iniciar.pack(pady=10)

        self.footer_label_inicial = tk.Label(self.frame_inicial, text="Feito por Karim Alzeben e Vinicius Nessler, para o curso de Engenharia de Software da Univille.", 
                                             bg="#2c2c2c", fg="white", font=("Helvetica", 10))
        self.footer_label_inicial.pack(side="bottom", pady=10)

        self.frame_titulo = None
        self.frame_perguntas = None
        self.frame_respostas = None
        self.frame_botoes = None
        self.frame_recomendacoes = None
        self.imagens = []

    def iniciar_quiz(self):
        self.frame_inicial.pack_forget()
        self.mostrar_quiz()

    def mostrar_quiz(self):
        self.frame_titulo = ttk.Frame(self.master)
        self.frame_titulo.pack(pady=10)

        self.label_titulo = tk.Label(self.frame_titulo, text="Quiz de Filmes", bg="#2c2c2c", fg="white", font=("Comic Sans MS", 24, "bold"))
        self.label_titulo.pack()

        self.frame_perguntas = ttk.Frame(self.master)
        self.frame_perguntas.pack(pady=20)

        self.label_pergunta = tk.Label(self.frame_perguntas, text="", wraplength=400, width=50, height=4,
                                       bg="#e0e0e0", fg="#000000", font=("Comic Sans MS", 14), relief="groove", bd=2, padx=10, pady=10)
        self.label_pergunta.grid(row=0, column=0, columnspan=2, pady=10)

        self.opcoes_respostas = ["Amo", "Gosto", "Indiferente", "Não Gosto", "Detesto"]
        self.respostas_vars = tk.StringVar(value=self.opcoes_respostas[2])

        self.frame_respostas = ttk.Frame(self.frame_perguntas)
        self.frame_respostas.grid(row=1, column=0, columnspan=2)

        self.radios = []
        for idx, opcao in enumerate(self.opcoes_respostas):
            radio = tk.Radiobutton(self.frame_respostas, text=opcao, variable=self.respostas_vars, value=opcao,
                                   bg="#2c2c2c", fg="white", font=("Comic Sans MS", 12), selectcolor="#00796b",
                                   indicatoron=0, width=15, height=2, relief="flat", bd=2, activebackground="#004d40")
            radio.grid(row=0, column=idx, padx=5, pady=10)
            self.radios.append(radio)

        self.frame_botoes = ttk.Frame(self.master)
        self.frame_botoes.pack(pady=10)

        self.btn_voltar = tk.Button(self.frame_botoes, text="Voltar", command=self.voltar_pergunta,
                                    bg="#b79a00", fg="white", font=("Comic Sans MS", 12), relief="flat", width=20, height=2)
        self.btn_voltar.grid(row=0, column=0, padx=10)
        self.btn_voltar.grid_forget()

        self.btn_responder = tk.Button(self.frame_botoes, text="Próxima Pergunta", command=self.responder,
                                       bg="#00796b", fg="white", font=("Comic Sans MS", 12), relief="flat", width=20, height=2)
        self.btn_responder.grid(row=0, column=1, padx=10)

        self.btn_detalhes = tk.Button(self.master, text="Mais Detalhes", command=self.toggle_detalhes,
                                      bg="#00796b", fg="white", font=("Comic Sans MS", 12), relief="flat", width=20, height=2)
        self.btn_detalhes.pack(pady=10)
        self.btn_detalhes.pack_forget()

        self.label_porcentagens = tk.Label(self.master, text="", bg="#2c2c2c", fg="#ffffff", font=("Comic Sans MS", 14))
        self.label_porcentagens.pack(pady=20)

        self.btn_refazer = tk.Button(self.master, text="Refazer Quiz", command=self.refazer_quiz,
                                     bg="#b79a00", fg="white", font=("Comic Sans MS", 12), relief="flat", width=20, height=2)
        self.btn_refazer.pack(pady=10)
        self.btn_refazer.pack_forget()

        self.footer_label = tk.Label(self.master, text="Feito por Karim Alzeben e Vinicius Nessler, para o curso de Engenharia de Software da Univille.", 
                                     bg="#2c2c2c", fg="white", font=("Helvetica", 10))
        self.footer_label.pack(side="bottom", pady=10)

        self.atualizar_pergunta()

    def responder(self):
        resposta = self.respostas_vars.get()
        if self.logic.responder(resposta):
            self.atualizar_pergunta()
        else:
            self.mostrar_resultado()
        self.btn_voltar.grid(row=0, column=0, padx=10)

    def voltar_pergunta(self):
        if self.logic.voltar_pergunta():
            self.atualizar_pergunta()
        if self.logic.current_question == 0:
            self.btn_voltar.grid_forget()

    def atualizar_pergunta(self):
        pergunta = self.logic.get_pergunta()
        self.label_pergunta.config(text=pergunta['pergunta'])
        self.respostas_vars.set(self.opcoes_respostas[2])

    def mostrar_resultado(self):
        self.btn_detalhes.pack()
        self.btn_refazer.pack(pady=(10, 20))
        self.frame_respostas.grid_forget()
        self.frame_botoes.pack_forget()

        self.ocultar_perguntas()

        pontuacao, contagem_generos = self.logic.calcular_pontuacao()
        porcentagens = self.logic.calcular_porcentagens(pontuacao, contagem_generos)

        self.label_porcentagens.config(text="Resultados:")
        self.exibir_cartazes(porcentagens)

    def exibir_cartazes(self, porcentagens):
        filmes_recomendados = self.selecionar_filmes(porcentagens)

        if self.frame_recomendacoes:
            self.frame_recomendacoes.destroy()

        self.frame_recomendacoes = ttk.Frame(self.master)
        self.frame_recomendacoes.pack(pady=20)

        label_subtitulo = tk.Label(self.frame_recomendacoes, text="Recomendações de filmes para você:", bg="#2c2c2c", fg="white", font=("Comic Sans MS", 18, "bold"))
        label_subtitulo.pack()

        self.frame_cartazes = ttk.Frame(self.frame_recomendacoes)
        self.frame_cartazes.pack(pady=30)

        self.imagens = []

        for filme in filmes_recomendados:
            try:
                image = Image.open(filme["imagem"])
                image = image.resize((100, 150), Image.LANCZOS)
                imagem = ImageTk.PhotoImage(image)
                self.imagens.append(imagem)

                frame_cartaz = ttk.Frame(self.frame_cartazes)
                frame_cartaz.pack(side="left", padx=10, pady=10)

                label_cartaz = tk.Label(frame_cartaz, image=imagem, bg="#2c2c2c")
                label_cartaz.pack()

                label_titulo = tk.Label(frame_cartaz, text=filme["titulo"], bg="#2c2c2c", fg="white", font=("Comic Sans MS", 12), wraplength=100)
                label_titulo.pack()
            except Exception as e:
                print(f"Erro ao carregar imagem {filme['imagem']}: {e}")

    def selecionar_filmes(self, porcentagens):
        generos_ordenados = sorted(porcentagens.items(), key=lambda x: x[1], reverse=True)

        filmes_recomendados = []
        for genero, _ in generos_ordenados:
            filmes_do_genero = [filme for filme in self.logic.filmes if genero in filme['genero']]
            random.shuffle(filmes_do_genero)
            if genero == generos_ordenados[0][0]:  # Gênero mais compatível
                filmes_recomendados.extend(filmes_do_genero[:3])
            elif genero == generos_ordenados[1][0]:  # Segundo mais compatível
                filmes_recomendados.extend(filmes_do_genero[:2])
            elif genero == generos_ordenados[2][0]:  # Terceiro mais compatível
                filmes_recomendados.extend(filmes_do_genero[:1])

        return filmes_recomendados

    def ocultar_perguntas(self):
        self.frame_perguntas.pack_forget()

    def toggle_detalhes(self):
        if self.detalhes_visiveis:
            self.ocultar_detalhes()
        else:
            self.mostrar_detalhes()

    def mostrar_detalhes(self):
        pontuacao, contagem_generos = self.logic.calcular_pontuacao()
        porcentagens = self.logic.calcular_porcentagens(pontuacao, contagem_generos)
        detalhes_ordenados = sorted(porcentagens.items(), key=lambda x: x[1], reverse=True)
        detalhes = ""
        for genero, porcentagem in detalhes_ordenados:
            detalhes += f"{genero.capitalize()}: {porcentagem:.2f}%\n"
        self.label_porcentagens.config(text=f"{self.label_porcentagens.cget('text')}\n\nDetalhes:\n{detalhes}")
        self.btn_detalhes.config(text="Ocultar Detalhes")
        self.detalhes_visiveis = True

    def ocultar_detalhes(self):
        resultado_texto = self.label_porcentagens.cget('text').split('\n\nDetalhes:')[0]
        self.label_porcentagens.config(text=resultado_texto)
        self.btn_detalhes.config(text="Mais Detalhes")
        self.detalhes_visiveis = False

    def refazer_quiz(self):
        self.logic.current_question = 0
        self.logic.respostas = []
        self.detalhes_visiveis = False
        self.label_porcentagens.config(text="")
        self.frame_perguntas.pack(pady=20)
        self.frame_respostas.grid()
        self.frame_botoes.pack(pady=10)
        self.btn_detalhes.pack_forget()
        self.btn_refazer.pack_forget()
        if self.frame_recomendacoes:
            self.frame_recomendacoes.destroy()
            self.frame_recomendacoes = None
        self.atualizar_pergunta()

        self.btn_voltar.grid(row=0, column=0, padx=10)
        self.btn_responder.grid(row=0, column=1, padx=10)

def main():
    perguntas = QuizLogic.carregar_perguntas('perguntas.json')
    logic = QuizLogic(perguntas)

    root = tk.Tk()
    app = QuizUI(root, logic)
    root.mainloop()

if __name__ == "__main__":
    main()
