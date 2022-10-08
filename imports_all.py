from flask import render_template, request, Flask, Blueprint, jsonify, redirect, url_for
import os
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user,login_required,current_user,logout_user
import uuid