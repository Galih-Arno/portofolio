from flask import Flask, render_template

app = Flask(__name__)

# Data contoh untuk proyek, Anda bisa menggantinya dengan data dari database atau sumber lainnya
projects_data = [
    {'id': 1, 'name': 'Project 1', 'description': 'Deskripsi lengkap tentang proyek 1', 'technologies': ['Flask', 'Tailwind CSS', 'JavaScript'], 'result': 'Proyek ini berhasil mencapai tujuan yang ditetapkan.'},
    {'id': 2, 'name': 'Project 2', 'description': 'Deskripsi lengkap tentang proyek 2', 'technologies': ['Django', 'Bootstrap', 'Python'], 'result': 'Proyek ini mengatasi masalah yang kompleks.'},
    {'id': 3, 'name': 'Project 3', 'description': 'Deskripsi lengkap tentang proyek 3', 'technologies': ['React', 'Node.js', 'Express'], 'result': 'Proyek ini menyederhanakan proses kerja.'}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route('/projects/<int:project_id>')
def details(project_id):
    # Cari proyek berdasarkan ID yang dipilih
    project = next((proj for proj in projects_data if proj['id'] == project_id), None)
    return render_template('details.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)
