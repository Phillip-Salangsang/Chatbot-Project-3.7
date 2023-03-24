from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)