import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Análise de Vendas - Papelaria")
        self.df = pd.DataFrame()

        # Botão para carregar arquivo CSV
        self.load_button = tk.Button(root, text="Carregar CSV", command=self.load_csv)
        self.load_button.pack(pady=10)

        # Tabela para mostrar os dados
        self.tree = ttk.Treeview(root, columns=("Produto", "Quantidade", "Valor Total"), show='headings')
        self.tree.heading("Produto", text="Produto")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Valor Total", text="Valor Total")
        self.tree.pack(pady=10)

        # Botão para mostrar análises
        self.analyze_button = tk.Button(root, text="Mostrar Análises", command=self.show_analysis)
        self.analyze_button.pack(pady=10)

        # Botão para mostrar gráfico de distribuição de preços
        self.plot_button = tk.Button(root, text="Distribuição de Preços", command=self.plot_price_distribution)
        self.plot_button.pack(pady=10)

        # Botão para mostrar gráfico de relação entre preço e quantidade
        self.scatter_button = tk.Button(root, text="Relação Preço x Quantidade", command=self.plot_price_quantity_relation)
        self.scatter_button.pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.update_table()
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar o arquivo: {e}")

    def update_table(self):
        # Limpar a tabela antes de adicionar novos dados
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for index, row in self.df.iterrows():
            self.tree.insert("", "end", values=(row["Produto"], row["Quantidade"], row["Valor Total"]))

    def show_analysis(self):
        if self.df.empty:
            messagebox.showwarning("Aviso", "Carregue um arquivo CSV primeiro.")
            return

        # Análises
        produtos_mais_vendidos = self.df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
        ticket_medio = self.df['Valor Total'].mean()
        frequencia_cliente = self.df['Cliente'].value_counts()

        # Exibir resultados
        analysis_text = f"Produtos Mais Vendidos:\n{produtos_mais_vendidos}\n\n"
        analysis_text += f"Ticket Médio: {ticket_medio:.2f}\n\n"
        analysis_text += f"Frequência de Compras:\n{frequencia_cliente}\n"

        messagebox.showinfo("Análises", analysis_text)

    def plot_price_distribution(self):
        if self.df.empty or 'Preço Unitário' not in self.df.columns:
            messagebox.showwarning("Aviso", "Carregue um arquivo CSV com a coluna 'Preço Unitário' primeiro.")
            return

        plt.figure(figsize=(10, 6))
        self.df['Preço Unitário'].plot(kind='hist', bins=10, alpha=0.7)
        plt.title('Distribuição de Preços dos Produtos Vendidos')
        plt.xlabel('Preço Unitário')
        plt.ylabel('Frequência')
        plt.grid(axis='y')
        plt.show()

    def plot_price_quantity_relation(self):
        if self.df.empty or 'Preço Unitário' not in self.df.columns or 'Quantidade' not in self.df.columns:
            messagebox.showwarning("Aviso", "Carregue um arquivo CSV com as colunas 'Preço Unitário' e 'Quantidade' primeiro.")
            return

        plt.figure(figsize=(10, 6))
        self.df.plot.scatter(x='Preço Unitário', y='Quantidade', alpha=0.7)
        plt.title('Relação entre Preço Unitário e Quantidade Vendida')
        plt.xlabel('Preço Unitário')
        plt.ylabel('Quantidade')
        plt.grid()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()
