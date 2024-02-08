from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mars():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(countdown_list)

@app.route('/image_mars')
def image():
    link = url_for('static', filename='mars.jpg')
    return """<!doctype html>
                       <html lang="en">
                         <head>
                           <meta charset="utf-8">
                           <title>Привет, Марс!</title>
                         </head>
                         <body>
                           <h1>Жди нас, Марс!</h1>
                           <img src={link} alt="здесь должна была быть картинка, но не нашлась">
                           <p>Вот он какая, красная планета.</p>
                         </body>
                       </html>""".format(link = link)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')