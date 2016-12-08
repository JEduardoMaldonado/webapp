import web
# @
from web import form
db = web.database(dbn='mysql', db='papeleria', user='root', pw='utec')
render=web.template.render('templates')
urls = (
    '/', 'login'
    ,'/index','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/ver/(.+)','ver',
    '/eliminar/(.+)','eliminar'
)

myformLogin = form.Form( 
    form.Textbox("usuario"), 
    form.Password("contrasena")
    )

myformPapeleria=form.Form(
    form.Textbox('Articulo'), 
    form.Textbox('Existencia'),
    form.Textbox('Marca'),
    form.Textbox('PrecioNeto'),
    form.Textbox('PrecioVenta'),
    form.Textbox('Ganancia')
)
class login:
    def GET(self):
        form = myformLogin()
        
        return render.login(form)
    
    def POST(self): 
        form = myformLogin()
        if not form.validates(): 
            return render.login(form)
        else: 
            result=db.select("login")
            dbuser=""
            dbPass=""
            for row in result:
                dbuser=row.usuario
                dbPass=row.contrasena

            if dbuser==form.d.usuario and dbPass==form.d.contrasena:
                raise web.seeother("/index")
            else:
               return render.error(form)

            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.

class index:
    def GET(self):
        
        result=db.select('productos')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew=myformPapeleria()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformPapeleria()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('productos', articulo=formNew.d.Articulo, 
            existencia=formNew.d.Existencia, marca=formNew.d.Marca,
             precioneto=formNew.d.PrecioNeto, precioventa=formNew.d.PrecioVenta, 
             ganancia=formNew.d.Ganancia)
            result=db.select('productos')
            raise web.seeother('/index')
            

class editar:
    def GET(self,id_articulo):
        formEdit=myformPapeleria()
        
        
        result=db.select('productos', where= "id_articulo=%s"%(id_articulo))
        
        for row in result:
            formEdit['Articulo'].value=row.articulo
            formEdit['Existencia'].value=row.existencia
            formEdit['Marca'].value=row.marca
            formEdit['PrecioNeto'].value=row.precioneto
            formEdit['PrecioVenta'].value=row.precioventa
            formEdit['Ganancia'].value=row.ganancia
        return render.editar(formEdit)        
    def POST(self,id_articulo):
        formEdit=myformPapeleria()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('productos', where='id_articulo=%s'%(id_articulo), articulo=formEdit.d.Articulo,
             existencia=formEdit.d.Existencia, marca=formEdit.d.Marca,
              precioneto=formEdit.d.PrecioNeto, precioventa=formEdit.d.PrecioVenta, ganancia=formEdit.d.Ganancia)
            result=db.select('productos')
            raise web.seeother('/index')
class eliminar:
    def GET(self,id_articulo):
        formEdit=myformPapeleria()
        
        result=db.select('productos', where='id_articulo=%s'%(id_articulo))
        
        for row in result:
            formEdit['Articulo'].value=row.articulo
            formEdit['Existencia'].value=row.existencia
            formEdit['Marca'].value=row.marca
            formEdit['PrecioNeto'].value=row.precioneto
            formEdit['PrecioVenta'].value=row.precioventa
            formEdit['Ganancia'].value=row.ganancia
        return render.eliminar(formEdit)        
    def POST(self,id_articulo):
        formEdit=myformPapeleria()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('productos', where="id_articulo=%s"%(id_articulo))
            raise web.seeother('/index')
class ver:
    def GET(self,id_articulo):
        
        result=db.select('productos', where="id_articulo=%s"%(id_articulo))
        return render.ver(result)

if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()