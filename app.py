from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Events
events = [
    {"id": 1, "name": "Tech Fest 2026", "date": "2026-12-15", "location": "Hyderabad", "description": "Annual tech festival with coding, robotics and workshops.", "seats": 100},
    {"id": 2, "name": "Hackathon", "date": "2026-12-20", "location": "Online", "description": "24 hours hackathon. Build amazing projects in teams.", "seats": 50},
    {"id": 3, "name": "Python Workshop", "date": "2026-12-25", "location": "Hyderabad", "description": "Learn Python from basics to advanced in one day.", "seats": 30},
]

registrations = []

@app.route('/')
def home():
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    return render_template('event.html', event=event)

@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    event = next((e for e in events if e['id'] == event_id), None)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        registrations.append({"name": name, "email": email, "phone": phone, "event": event['name']})
        return render_template('success.html', name=name, event=event)
    return render_template('register.html', event=event)

@app.route('/my-registrations')
def my_registrations():
    return render_template('my_registrations.html', registrations=registrations)

@app.route('/cancel/<int:index>')
def cancel(index):
    if 0 <= index < len(registrations):
        registrations.pop(index)
    return redirect(url_for('my_registrations'))

if __name__ == '__main__':
    app.run(debug=True)