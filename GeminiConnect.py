from flask import Flask, jsonify, request
from flask_cors import CORS
import creds
import textwrap, os
import google.generativeai as genai