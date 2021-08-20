from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

error_bp = Blueprint('error_bp', __name__)


# @error_bp.route('/')
@error_bp.route('/not_found')
def not_found():
    return {"Error": "not found"}
