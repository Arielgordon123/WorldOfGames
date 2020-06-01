pipeline {
    agent any
    stages {
        stage('Checkout the repository.') {
            steps {
                git(
                    url: 'https://github.com/Arielgordon123/WorldOfGames.git',
                    branch: 'test'
                    )
            }
        }
        stage('Build docker image') {
            steps {
                sh 'echo $(( ( RANDOM % 999 )  + 1 )) > src/Scores.txt'
                sh 'docker build -t arielgordon/worldofgames .'
            }
        }
        stage('Run docker image') {
            steps {
                sh 'docker run -d -p 8777:5000  arielgordon/worldofgames'
            }
        }
        stage('Test') {
            steps {
                sh 'cd src && pipenv --python /usr/bin/python3 lock --requirements > requirements.txt'
                sh 'pip3 install -r requirements.txt'
                sh 'echo APP_URL=http://localhost:8777 > src/.env'
                sh 'python3 tests/e2e.py'
            }
        }
    }
}
