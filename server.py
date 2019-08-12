#!/usr/bin/env python
#!/usr/bin/python
from flask import Flask, request, jsonify, render_template, send_file
from flask_restful import Resource, Api
from json import dumps
import os
import traceback
import json
import socket
import MySQLdb
import database_utility
from datetime import datetime

app = Flask(__name__)
api = Api(app)
#hostname = socket.gethostname()
#IPAddr=socket.gethostbyname(hostname)
#print("Your Computer Name is:"+hostname)
#print("Your Computer IP Address is:"+IPAddr)

@app.route('/')
def shortenedPage():
    return render_template("shortened.html")

@app.route('/shortenedLinks')
def getShortenedLinks():
    print "Get Shortened Links API Entering....."
    links_dictionary = {}
    shortened_links_list = []
    original_links_list = []
    databaseConnection = database_utility.databaseConnection()
    cursor = databaseConnection.cursor()
    query = "SELECT shortened_link, original_link FROM ShortenedLinks"
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        print "records.........", records
        for record in records:
            shortened_links_list.append(record[0])
            original_links_list.append(record[1])
        links_dictionary = {"shortened_links": shortened_links_list, "original_links": original_links_list}
    except (MySQLdb.IntegrityError,MySQLdb.ProgrammingError,MySQLdb.DataError,MySQLdb.OperationalError,MySQLdb.NotSupportedError,MySQLdb.InternalError) as exception:
        print "Error in:::", exception
        print(traceback.format_exc())
    finally:
        databaseConnection.close()
        cursor.close()
    return links_dictionary

if __name__ == '__main__':
    app.run(host= '192.168.43.67', port='2020')
