pipeline {
    agent any
    stages {
        stage('Checkout the repository.') {
            steps {
                git(
                    url: 'https://github.com/Arielgordon123/WorldOfGames.git',
                    branch: 'master'
                    )
            }
        }
        stage('Build docker image') {
            steps {
                sh 'echo $(( ( RANDOM % 999 )  + 1 )) > /app/src/Scores.txt'
                sh 'docker build -t arielgordon/WorldOfGames .'
            }
            stage('Run docker image') {
                steps {
                    sh 'docker run -d -p 8777:5000  arielgordon/WorldOfGames .'
                }
            }
        }
    }
}
