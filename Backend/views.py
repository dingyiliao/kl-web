from flask import (Blueprint,
                   render_template, 
                   request)

views_blueprint = Blueprint('views', __name__)


@views_blueprint.route('/')
def homepage():
    return render_template('home-page.html', page_title='home')


@views_blueprint.route('/listening')
def listening():
    return render_template('listening-page.html', page_title='listening')


@views_blueprint.route('/reading')
def reading():
    return render_template('reading-page.html', page_title='reading')


@views_blueprint.route('/writing')
def writing():
    return render_template('writing-page.html', page_title='writing')


@views_blueprint.route('/gym')
def gym():
    return render_template('gym-page.html', page_title='gym')
