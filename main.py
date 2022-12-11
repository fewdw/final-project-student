import pymongo as pymongo
from flask import Flask, request, jsonify
from pymongo.server_api import ServerApi
from flask_cors import CORS