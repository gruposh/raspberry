from bottle import route, run, template

@route('/bbq/sensors/temp/<sensorId>')
def temp(sensorId):
    return template('sensor {{sensorId}} value', sensorId=sensorId)

run(host='localhost', port=8080)