from os import environ

from flask import Blueprint, redirect, url_for
from flask_oidc import OpenIDConnect
from okta import UsersClient


bp = Blueprint("auth", __name__, url_prefix="/")
oidc = OpenIDConnect()
okta_client = UsersClient("{{ OKTA_ORG_URL }}", "{{ OKTA_AUTH_TOKEN }}")


@bp.route("/login")
@oidc.require_login
def login():
    """
    Force the user to login, then redirect them to the dashboard.
    """
    return redirect(url_for("blog.dashboard"))


@bp.route("/logout")
def logout():
    """
    Log the user out of their account.
    """
    oidc.logout()
    return redirect(url_for("blog.index"))
