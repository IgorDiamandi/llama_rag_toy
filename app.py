from flask import Flask, request, render_template
from markupsafe import Markup
from starter import get_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.form.get('question')
    response = get_response(user_question)
    formatted_response = str(response).replace("\n", "<br><br>")
    bot_message_html = f'<div class="message bot-message">{formatted_response}</div>'
    return Markup(bot_message_html)


if __name__ == '__main__':
    app.run(debug=True)
