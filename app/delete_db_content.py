from flask import Flask, Blueprint, render_template, redirect, request, url_for, flash, session

#SCRIPT pozwala usuwać zawartosc bazy danych!
with app.app_context():
    # Usuń wszystkich uczestników
    db.session.query(Participants).delete()
    db.session.commit()