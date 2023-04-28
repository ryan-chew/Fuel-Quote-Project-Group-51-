from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect
from flask_login import login_required, current_user
from .models import Quote 
from .models import ClientInformation
from .models import User
from . import db
import json
from datetime import datetime
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if (current_user.profile):
        if request.method == 'POST': 
            gallons = request.form.get('gallons', type=int)
        
            address = current_user.profile[0].address1 
            date = request.form.get('date') 

            state_factor = .02 if(current_user.profile[0].state=="TX") else .04 
            rate_factor = .01 if(current_user.quotes) else 0 
            gallons_factor = .02 if(gallons >1000 ) else .03 
            profit_factor = .10 
            profit_margin = (state_factor - rate_factor + gallons_factor + profit_factor)*1.5

            price_to_gallon = profit_margin + 1.5
            cost = gallons * price_to_gallon
            
            quote = Quote(gallons = gallons, address = address, date = date, cost = cost, 
            user_id =current_user.id)
            if ("save" in request.form):
                db.session.add(quote)
                db.session.commit()
            return render_template("quote.html", user=current_user, cost = cost, price_to_gallon = price_to_gallon, gallons = gallons, date = date) 
        return render_template("quote.html", user=current_user, cost = 0, price_to_gallon = 0, gallons = 0, date = "2023-01-01")
    else:   
        flash('Please create a profile, try again.')
        return redirect(url_for('auth.profile')) 

@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():
    if (current_user.profile):
        quotes = Quote.query.filter(Quote.user_id == current_user.id).all()
    
        return render_template("history.html", user=current_user, quotes = quotes)

    else:
        flash('Please create a profile, try again.')
        return redirect(url_for('auth.profile'))


