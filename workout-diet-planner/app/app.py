from flask import Flask, request, jsonify
from models.user import User
from models.workout import Workout
from models.diet import Diet

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        user_data = request.form
        user = User(user_data['name'], user_data['age'],  float(user_data['weight']), float(user_data['height']))
        workout = Workout(user)
        diet = Diet(user)

        return jsonify({
            'workout': workout.generate_workout_plan(),
            'diet': diet.generate_diet_plan()
        })

if __name__ == '__main__':
    app.run(debug=True)