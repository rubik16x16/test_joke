from ast import arg
from flask import Flask
from flask import request
from flask import Response
import requests

from sqlalchemy import create_engine, null
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.orm import Session
from sqlalchemy import select

Base = declarative_base()

engine = create_engine('mysql://root:secret@localhost:3306/test_flask')

class Joke(Base):
	__tablename__ = 'jokes'
	id = Column(Integer, primary_key=True)
	joke = Column(Text)

	def __repr__(self):
		return '<Joke %r>' % self.joke

app = Flask(__name__)

@app.route('/jokes/<joke_type>')
def joke(joke_type):

	if joke_type == 'Chuck':
		res = requests.get('https://api.chucknorris.io/jokes/random')
		data = res.json()
		return data['value']
	elif joke_type == 'Dad':

		res = requests.get('https://icanhazdadjoke.com/', headers={
			'Accept': 'application/json'
		})
		data = res.json()
		return data['joke']

	return "Joke type doesn't exist", 400

@app.route('/jokes', methods=['POST'])
def store():
	if request.method == 'POST':
		data = request.get_json()
		joke = Joke(joke=data['joke'])
		with Session(engine) as session:
			session.add(joke)
			session.commit()
			return Response(null, 201)

@app.route('/jokes/<number>', methods=['PUT', 'DELETE'])
def update(number):
	if request.method == 'PUT':
		data = request.get_json()
		with Session(engine) as session:
			stmt = select(Joke).where(Joke.id == number)
			joke = session.scalar(stmt)
			joke.joke = data['joke']
			session.commit()
			return Response(null, 200)

	if request.method == 'DELETE':
		with Session(engine) as session:
			joke = session.get(Joke, number)
			session.delete(joke)
			session.commit()
			return Response(null, 200)

@app.route('/mcm')
def mcm():
	args = request.args

	num1 = int(args['number1'])
	num2 = int(args['number2'])

	a = max(num1, num2)
	b = min(num1, num2)

	while b:
		mcd = b
		b = a % b
		a = mcd
	mcm = (num1 * num2) // mcd

	return 'MCM {0}'.format(mcm)

@app.route('/next')
def next_number():

	args = request.args

	return 'Number {0}'.format(int(args['number']) + 1)
