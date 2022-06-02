# aiohttpdemo_polls/routes.py
import pathlib

from views import index, poll, results, vote, add_form, add_poll


PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    app.router.add_get('/', index, name="index")
    app.router.add_get('/poll/{question_id}', poll, name="poll")
    app.router.add_get('/poll/{question_id}/results', results, name="results")
    app.router.add_get('/add_form', add_form, name="add_form")
    app.router.add_post('/poll/{question_id}/vote', vote, name='vote')
    app.router.add_post('/add_form/add', add_poll, name="add_poll")
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static',
                          path=PROJECT_ROOT/'static',
                          name='static')
