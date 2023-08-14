from flask import (Blueprint,
                   jsonify)

services_blueprint = Blueprint('services', __name__)


@services_blueprint.route('/total_num')
def api1():
    return jsonify({
        'num': 2,
        'name': 'Jack',
        'detail': {
            'rank': 3,
            'activity': 'GWP'
        }
    })
