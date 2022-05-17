import requests
from sqlalchemy.orm import Session
from sqlalchemy import select
from jokes import engine, Joke

def test_joke():
	res = requests.get('http://localhost:5000/jokes/Dad')
	assert res.status_code == 200

	res = requests.get('http://localhost:5000/jokes/Chuck')
	assert res.status_code == 200

	res = requests.get('http://localhost:5000/jokes/Dads')
	assert res.status_code == 400

def test_store_joke():

	res = requests.post('http://localhost:5000/jokes', json={'joke': 'unit test'})
	assert res.status_code == 201

def test_update_joke():

	with Session(engine) as session:
		joke = session.query(Joke).first()

	res = requests.put('http://localhost:5000/jokes/{0}'.format(joke.id), json={'joke': 'unit testx'})
	assert res.status_code == 200

def test_delete_joke():

	with Session(engine) as session:
		joke = session.query(Joke).first()

	res = requests.delete('http://localhost:5000/jokes/{0}'.format(joke.id), json={'joke': 'unit testx'})
	assert res.status_code == 200

def test_mcm():

	res = requests.get('http://localhost:5000/mcm', params={'number1': 2, 'number2': 3})
	assert res.status_code == 200
	assert res.text == 'MCM 6'

def test_next():

	res = requests.get('http://localhost:5000/next', params={'number': 1})
	assert res.status_code == 200
	assert res.text == '2'
