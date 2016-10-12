# bball_angular

http://owaislone.org/blog/webpack-plus-reactjs-and-django/

Since we are using pure webpack without any abstraction, we are free to use it however we want without the need to integrate any special with django. Whenever something new comes up for webpack, we can immediately use it without worrying if staticfiles, pipeline or compressor will support it or not. Decoupling is good!


Using react-hot-loader means any changes made to the react components will reflect in the browser. No reload needed! We need webpack-dev-server to build and serve our bundles in order to hot reload any modules.


## To run locally

pip install -r requirements.txt
python manage.py runserver
node server.js


