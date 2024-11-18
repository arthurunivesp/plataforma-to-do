from flask import Flask, render_template, request, redirect, url_for, session, flash
import pg8000
import re
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seu_email@example.com'
app.config['MAIL_PASSWORD'] = 'sua_senha'

mail = Mail(app)

def get_db_connection():
    try:
        conn = pg8000.connect(
            database="plataforma_todo",
            user="seu_usuario",
            password="admin123",
            host="localhost",
            port=5432
        )
        return conn
    except pg8000.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        flash(f"Erro ao conectar ao banco de dados: {e}")
        return None
    except Exception as e:
        print("Erro inesperado ao conectar ao banco de dados:", e)
        flash(f"Erro inesperado ao conectar ao banco de dados: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user:
                session['user_id'] = user[0]
                return redirect(url_for('trilhas'))
            else:
                flash("Usuário ou senha incorretos!")
                return redirect(url_for('home'))
        except Exception as e:
            print("Erro ao acessar o banco de dados:", e)
            flash("Ocorreu um erro ao tentar logar. Tente novamente.")
            return redirect(url_for('home'))
    else:
        flash("Não foi possível conectar ao banco de dados.")
        return redirect(url_for('home'))

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/register', methods=['POST'])
def register():
    primeiro_nome = request.form['primeiro_nome']
    ultimo_nome = request.form['ultimo_nome']
    data_nascimento = request.form['data_nascimento']
    usuario = request.form['usuario']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$', senha):
        flash("A senha deve ter pelo menos 8 caracteres, incluindo uma letra maiúscula, um número e um símbolo especial.")
        return redirect(url_for('cadastro'))
    
    if senha != confirmar_senha:
        flash("As senhas não coincidem. Tente novamente.")
        return redirect(url_for('cadastro'))

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
            user = cursor.fetchone()
            if user:
                flash("Usuário já cadastrado. Tente outro nome de usuário.")
                return redirect(url_for('cadastro'))

            cursor.execute(
                "INSERT INTO usuarios (primeiro_nome, ultimo_nome, data_nascimento, usuario, senha) VALUES (%s, %s, %s, %s, %s)", 
                (primeiro_nome, ultimo_nome, data_nascimento, usuario, senha)
            )
            conn.commit()
            cursor.close()
            conn.close()
            flash("Cadastro realizado com sucesso! Por favor, faça o login.")
            return redirect(url_for('home'))
        except Exception as e:
            print("Erro ao inserir no banco de dados:", e)
            flash(f"Ocorreu um erro ao cadastrar: {e}")
            return redirect(url_for('cadastro'))
    return redirect(url_for('cadastro'))

@app.route('/trilhas')
def trilhas():
    if 'user_id' in session:
        return render_template('trilhas.html')
    return redirect(url_for('home'))

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        # Aqui você pode adicionar a lógica para verificar se o e-mail existe no banco de dados
        # e gerar um token de redefinição de senha, por exemplo
        msg = Message('Redefinição de Senha', sender='seu_email@example.com', recipients=[email])
        msg.body = 'Clique no link para redefinir sua senha: <link>'
        mail.send(msg)
        flash('E-mail de redefinição de senha enviado. Verifique seu e-mail.')
        return redirect(url_for('home'))
    return render_template('esqueci_senha.html')

if __name__ == '__main__':
    app.run(debug=True)
