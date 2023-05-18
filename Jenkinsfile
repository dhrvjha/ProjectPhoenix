pipeline {
    agent {
        docker {image 'python:slim-bullseye'}
    }
    options {
        timeout(time: 1, unit: "SECONDS")
    }
    stages {
        stage ("Build") {
            steps {
                echo "Hello World"
            }
        }
    }
}