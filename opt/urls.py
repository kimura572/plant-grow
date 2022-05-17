from controllers import *
 
 
# FastAPIのルーティング用関数
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
app.add_api_route('/home', home)
app.add_api_route('/tr', tr)