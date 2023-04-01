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
    if request.method == 'POST': 
        gallons = request.form.get('gallons', type=int)
        address = current_user.profile[0].address1 #need to display this on html? 
        date = request.form.get('date') #currently a string cant get it to be "date" data type
              #store pricing per gallon/display on html 
        price_per = 3 
        cost = gallons * price_per 
        quote = Quote(gallons = gallons, address = address, date = date, cost = cost, 
        user_id =current_user.id)
        db.session.add(quote)
        db.session.commit()
        return redirect(url_for('views.home')) #needs to point to history.html once that works 
    return render_template("quote.html", user=current_user)



