from flask import Flask, jsonify, request
from flask_cors import CORS
import creds
import textwrap, os
import google.generativeai as genai

my_api_key= creds.gemini_api_key
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)
CORS(app)

def generate_playlist(prompt):
    
    try:
        response=model.generate_content(prompt)
        generated_text=response.text
        
        return generated_text
    except Exception as e:
        return "Error fetching calculations:{e}"