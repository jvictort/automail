import smtplib
import email.message
import pandas as pd

def send_email(quantify, product, provider_email):
    email_body = f"""
                    <p>Este é um e-mail automático enviado com Python!</p>
                    <p>Olá, gostaria de solicitar um pedido de {quantify} unidade(s) de {product}(s)</p>
                    <p>Abs,</p>
                    <p>João Victor.</p>
                 """

    message = email.message.Message()

    message["Subject"] = f"Pedido de compras de {product}"
    message["From"] = "seu_email"
    message["To"] = f"{provider_email}"

    from_password = "sua_senha"

    message.add_header("Content-Type", "text/html")
    message.set_payload(email_body)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()

    s.login(message["From"], from_password)

    s.sendmail(message["From"], [message["To"]], message.as_string().encode("utf-8"))

    print("Email enviado.")

data = pd.read_excel("./Files/Fornecedores.xlsx", engine="openpyxl")

for i in range(len(data)):
    product_stock = data["Qtd. Estoque"][i]
    product_sales = data["Qtd. De vendas previstas"][i]

    diff = product_stock - product_sales

    if diff < 0:
        send_email((-diff), data["Produtos"][i], data["Fornecedores"][i])
