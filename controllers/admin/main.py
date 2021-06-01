from run import app
from flask import render_template,redirect,request,url_for
@app.route('/admin')
def admin_index():
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template('admin/index.html')
    else:
        return redirect(url_for('login'))


    