from flask import Flask, request, redirect, url_for, Blueprint, render_template

homepage = Blueprint("homepage", __name__, static_folder="static", template_folder="templates")

@homepage.route("/", methods=['GET'])
def index():
	return render_template('homepage/index.html')

@homepage.route("/userdashboard", methods=['GET'])
def userindex():
	return render_template('user/userindex.html')

