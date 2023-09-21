#import os untuk mengakses sistem database
import os

#import sql untuk menggunakan bahasa sql dalam python
from cs50 import SQL
#import tools untuk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

#mengatur nama aplikasi
app = Flask(__name__)

#dipakai untuk koneksi kedatabase
db = SQL("sqlite:///birthdays.db")

#http://127.0.0.1:5000/
@app.route ("/", methods=["GET", "POST"])
#ketika route "/" dipanggil/diakses, maka fungsi index() dieksekusi
def index():
    #jika request yang dilakukan  oleh pengguna adalah post, maka eksekusi kode dalam if 
    if request.method == "POST":

        #access form data/membaca data yang diisikan pada form
        name = request.form.get("name")#ambil daa dari imput nama
        month = request.form.get("month")#ambil data dari imput month
        day = request.form.get("day")#ambil data dari imput day

        #insert data into database, masukkan data name, month, dan day ke database
        db.execute("INSERT INTO birthdays (name,month, day) VALUES(?,?,?)", name, month, day)
        #go back to homepage, balik ke https://127.0.0.1:5000/
        return redirect("/")

    #jika requestnya selain post, maka tampilkan data dari tabel birthdays
    else:
        #ambil seluruh data dari tabel birthdays, simpan di variabel birthdays 
        birthdays = db.execute("SELECT * FROM birthdays")

        #salin isi variable birthdays ke birthdays, lalu kirim ke index.html
        return render_template("index.html",
        birthdays=birthdays)
        

