pipeline {
    agent any
    environment {
        registry = 'arielgordon/worldofgames'
        registryCredential = 'dockerhub'
    }
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
                sh 'echo $(( ( RANDOM % 999 )  + 1 )) > src/Scores.txt'
                script {
                    dockerImage = docker.build registry + ':$BUILD_NUMBER'
                }
            // sh 'docker build -t arielgordon/worldofgames .'
            }
        }
        stage('Run docker image') {
            steps {
                sh 'docker run -d -p 8777:5000 --name worldofgames  arielgordon/worldofgames'
            }
        }
        stage('Test') {
            steps {
                sh 'cd src && pipenv --python /usr/bin/python3 lock --requirements > requirements.txt'
                sh 'pip3 install -r src/requirements.txt'
                sh 'echo APP_URL=http://localhost:8777 > src/.env'
                sh 'python3 src/tests/e2e.py'
            }
        }
    }
    post {
        always {
            echo 'Finalize'
            script {
                docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                }
            }
            sh 'docker rm -f worldofgames'
            sh 'docker rmi $registry:$BUILD_NUMBER'
        }
    }
}
