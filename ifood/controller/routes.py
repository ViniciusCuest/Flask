from flask import Flask, render_template, request

def init(instance: Flask):
    @instance.route('/')
    def index():
        return render_template('index.html')

    @instance.route('/foods')
    def foods():
        return render_template('foods.html')

    @instance.route('/orders')
    def orders():
        return render_template('orders.html')

    @instance.route('/profile')
    def profile():
        return render_template('profile.html')