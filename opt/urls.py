from controllers import *
 
 
# FastAPIのルーティング用関数
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
app.add_api_route('/start', start)
app.add_api_route('/s', new)